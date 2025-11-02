from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ChromeDriver 실행
browser = webdriver.Chrome()

# 암시적 기다림 설정 (최대 10초)
browser.implicitly_wait(10)

# 트위터 계정 페이지로 이동
twitter_account_url = 'https://x.com/kube_z?s=21&t=bKR84PX8-bgKKFAyFP5w-Q'  # 원하는 계정명 입력
browser.get(twitter_account_url)

# 페이지 로딩 대기
time.sleep(5)
tweet_contents = set()

# 답글 제한 없음으로 뜸
def check_reply_limit(tweet):
    try:
        reply_button = WebDriverWait(tweet, 10).until(
            EC.presence_of_element_located((By.XPATH, './/button[@data-testid="reply"]'))
        )
        svg_element = reply_button.find_element(By.TAG_NAME, 'svg')
        svg_classes = svg_element.get_attribute('class').split()
        print(f"SVG classes: {svg_classes}")
        if 'r-12c3ph5' in svg_classes:
            return "답글 제한됨"
        else:
            return "제한 없음"
    except Exception as e:
        print(f"답글 제한 확인 실패: {e}")
        return "확인 불가"


def scroll_and_collect_tweets(browser, max_tweets):
    tweets_data = []
    processed_tweets = set()
    last_height = browser.execute_script("return document.body.scrollHeight")

    while len(tweets_data) < max_tweets:
        # 부분 스크롤 범위 확대
        browser.execute_script("window.scrollBy(0, 3000);")
        time.sleep(5)  # 대기 시간을 5초로 늘림

        # 새로운 트윗 로드 대기
        try:
            WebDriverWait(browser, 15).until(
                lambda x: len(browser.find_elements(By.CSS_SELECTOR, 'article')) > len(processed_tweets)
            )
        except TimeoutException:
            print("새로운 트윗을 로드하는 데 시간이 초과되었습니다.")

        # 트윗 요소들 찾기
        tweets = browser.find_elements(By.CSS_SELECTOR, 'article')

        for tweet in tweets:
            if len(tweets_data) >= max_tweets:
                break

            try:
                # 트윗 내용
                tweet_text_element = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
                tweet_text = tweet_text_element.text if tweet_text_element else "내용 없음"

                # 중복 트윗인지 확인
                if tweet_text in tweet_contents:
                    continue  # 이미 처리한 트윗은 무시
                tweet_contents.add(tweet_text)

                try:
                    retweet_count_element = tweet.find_element(By.XPATH, './/div[2]/button/div/div[2]/span/span/span')
                    retweet_count = retweet_count_element.text
                    print(f"리트윗 수: {retweet_count}")
                except Exception as e:
                    print(f"리트윗 수 추출 실패: {e}")
                    retweet_count = '0'

                try:
                    account_name_element = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"] span')
                    account_name = account_name_element.text
                except NoSuchElementException:
                    account_name = '이름 없음'
                # 게시물 수 가져오기
                try:
                    post_count_element = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, 'div[class*="css-146c3p1"][style*="color: rgb(113, 118, 123)"]'))
                    )
                    post_count = post_count_element.text.split()[0]  # "524 posts"에서 숫자만 추출
                except Exception as e:
                    print(f"게시물 수 추출 실패: {e}")
                    post_count = "알 수 없음"

                reply_limit_status = check_reply_limit(tweet)

                tweets_data.append({
                    '계정 이름': account_name,
                    '트윗 내용': tweet_text,
                    '리포스트 수': retweet_count,
                    '답글 제한 여부': reply_limit_status,
                    '작성한 포스트 수': post_count
                })


                print(f"수집된 트윗 수: {len(tweets_data)}")

            except Exception as e:
                print(f"트윗 처리 중 에러 발생: {e}")

        # 페이지 끝에 도달했는지 확인
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("페이지 끝에 도달했습니다.")
            break
        last_height = new_height

    return tweets_data

# 트윗 수집 실행
max_tweets = 200 #희망개수
tweets_data = scroll_and_collect_tweets(browser, max_tweets)

# 브라우저 종료
browser.quit()

# DataFrame으로 변환
df = pd.DataFrame(tweets_data)

# CSV 파일로 저장
df.to_csv('크롤링.csv', index=False, encoding='utf-8-sig')

print("크롤링 완료 및 CSV 파일 저장 완료!")