import csv
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# ChromeDriver 실행
browser = webdriver.Chrome()

# 트위터 로그인 페이지로 이동
twitter_login_url = 'https://x.com/login'
browser.get(twitter_login_url)

# 로그인 시간을 충분히 줌 (30초)
print("트위터에 수동으로 로그인하세요.")
input("로그인 완료 후 Enter 키를 눌러주세요 ...")

# 수집할 트윗 링크 리스트
tweet_urls = [
'https://x.com/foodie_archive/status/1825770632342286823',
'https://x.com/foodie_archive/status/1833008561116618865',
'https://x.com/foodie_archive/status/1780073995863457991',
'https://x.com/foodie_archive/status/1780189384203293180',
'https://x.com/foodie_archive/status/1777160548305850639',
'https://x.com/foodie_archive/status/1793300616623927545',
'https://x.com/foodie_archive/status/1800404127446712669',
'https://x.com/foodie_archive/status/1783056067532132464',
'https://x.com/foodie_archive/status/1773549915626422574',
'https://x.com/foodie_archive/status/1782683784594526280',
'https://x.com/foodie_archive/status/1785138290942980509',
'https://x.com/foodie_archive/status/1826909927018725753',
'https://x.com/foodie_archive/status/1810217235916767292',
'https://x.com/foodie_archive/status/1839515640513884480',
'https://x.com/foodie_archive/status/1843243908933058576',
'https://x.com/foodie_archive/status/1780423777354232016',
'https://x.com/foodie_archive/status/1779510583479746707',
'https://x.com/foodie_archive/status/1826439718772543532',
'https://x.com/foodie_archive/status/1781657853444735094',
'https://x.com/foodie_archive/status/1808319616709714141',
'https://x.com/foodie_archive/status/1786304514683027601',
'https://x.com/foodie_archive/status/1831154502390694001'
]

# 수집할 계정 목록
target_accounts = {
    "@sinsang_info",
    "@jalmukkk",
    "@yx2n_s",
    "@isitrigwa",
    "@cod_2B",
    "@coskiriful",
    "@Ihavelotsoflove",
    "@mys80_",
    "@foodie_archive",
    "@feedforyou11",
    "@iiioiii13",
    "@of313_",
    "@mood_swiing",
    "@food_archiving",
    "@yu1_1n",
    "@wat2r_t2",
    "@summer_neung",
    "@okas_ia",
    "@snowdoesnot",
    "@dokjjang_good",
    "@BBERRY_V",
    "@suzu_kiring",
    "@abc10293888",
    "@forblue_",
    "@yu1_1n",
    "@damgooom",
	'@il_lite',
	'@parkkodeok',
	'@tiewis__su',
	'@orezzol',
	'@ohhhpu',
	'@22eiu',
	'@churroblue',
	'@nana__1075',
	'@newspicy1214',
	'@yeye_muk',
	'@yon99yon',
	'@nyauxuo',
	'@p0tat0_motd',
	'@na_irong',
	'@yenanyong',
	'@eat_slolo',
	'@Tqe0E',
	'@js9613100',
	'@chou_213',
	'@dear_my_darl',
	'@irisshopped',
	'@d1azz1e_',
	'@bambbbang_',
	'@cosmeticduck_lv',
	'@peach3848',
	'@roblerob10',
	'@abcd1ovee',
	'@beep_beep_00',
	'@yum_good_yum',
	'@meowww_111',
	'@dxxoxcos',
	'@feedforyou11',
	'@hgien23',
	'@nalalop81',
	'@noopnoop__',
	'@youuth0340',
	'@xiverez',
	'@omgjimi',
	'@sugarnutcracker',
	'@soreisord',
	'@9nof6',
	'@isyourx_',
	'@dorotice5',
	'@ae_zxrx',
	'@theonly_o_ne',
	'@soophhhhhy',
	'@il_lite',
	'@sunggnyungg',
	'@itisjuyjuy',
	'@iloveexxxz',
	'@_mmmmmakeup',
	'@kyaco111',
	'@huu_odiga',
	'@mokabob_',
	'@imprettypoor',
	'@damgooom',
	'@lovyourscene',
	'@youucrazy_',
	'@meullioiio',
	'@pmmpem',
	'@lovelorn__v',
	'@dangedange31',
	'@betdogsun',
	'@kimyulgyo_',
	'@elin96__k',
	'@coscrazy_Girl',
	'@ToolTravle',
	'@ma__verite',
	'@WLo6r',
	'@tamasigsalog',
	'@d00_xxc3',
	'@k1yo_ya',
	'@lemoncafri',
	'@cloud__luvxx',
	'@alis__S2',
	'@_dawnclouds',
	'@urthebestp',
	'@v2nc0uver',
	'@c0c0s23',
	'@coko38',
	'@won_nkl',
	'@sanseey_',
	'@mongsilXmu',
	'@day3muk',
	'@rimieeeezzang',
	'@malaeng33',
	'@miu929283',
	'@forblue_',
	'@mymunge',
	'@imdpwls_o',
	'@mUegoing',
	'@gghhh2131',
	'@bora_na29',
	'@pinkumarsh',
	'@happier_than_UR',
	'@fig_mute',
	'@yeobeun__ii',
	'@nora_me_',
	'@sappipii',
	'@PINKS2ODA',
	'@pjyiskra',
	'@thisisme_won',
	'@rlamerong3',
	'@0ozxe',
	'@gnn_ottd',
	'@vollygay',
	'@LouidNoi',
	'@rnehrgmfrp',
	'@cherishllie',
	'@recordboookofme',
	'@intheruthless',
	'@skydell82',
	'@mmnInj9',
	'@berryveryhe__',
	'@manduuuu__u',
	'@__sulhyang',
	'@W83zN',
	'@c0c0s23',
	'@meowww_111',
	'@nohara_bira',
	'@xxxzgu',
	'@cos_mimmi',
	'@c02rar',
	'@psyche1102',
	'@cosmevvid',
	'@bab_10000',
	'@Side_to_us',
	'@baek480',
	'@yeoul_ss',
	'@zperkki',
	'@sso__ssweet',
	'@rozearozy',
	'@sobom_cos',
	'@kitty112929',
	'@SakiDoskim',
	'@pinaco_swatch',
	'@JJ_05_JJ',
	'@ha7l10',
	'@googooppe',
	'@_honeytip',
	'@chymoly',
	'@iamloveallpink',
	'@im_andim',
	'@eeyoungo',
	'@yex_n1',
	'@disarr',
	'@mmnInj9',
	'@woowin__1',
	'@babymoomoomin',
	'@sphe_c5',
	'@sakaoii',
	'@gunw00kii',
	'@Moru_S2_',
	'@hitnrunwh',
	'@poi_1012',
	'@pinkmoxhi',
	'@still_cozy',
	'@an1ndeyo',
	'@an_347ml',
	'@Oooi0983',
	'@yournalee',
	'@solig_ht',
	'@yjmok1992',
	'@LouidNoi',
	'@only1intheearth',
	'@lusidval',
	'@imyeongja725275',
	'@myommww',
	'@BOBOB_911',
	'@yujjang8',
	'@F6EuHTr',
	'@elin96__k',
	'@3bLA89'}

# 결과 저장용 리스트 초기화
all_tweets_data = []

for tweet_url in tweet_urls:
    # 트윗 페이지로 이동
    browser.get(tweet_url)
    time.sleep(10)  # 페이지 로딩 대기

    # 트윗 텍스트 수집
    tweet_text_element = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
    tweet_text = tweet_text_element.text
    print(tweet_text)

    # 계정명 수집
    account_name_element = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"] span')
    account_name = account_name_element.text
    print(account_name)

    # 트윗 작성자 ID 수집
    text_content_element = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/a/div/span')
    text_content = text_content_element.text
    print(text_content)

    # 인용 계정 수집
    quote_acc = set()
    quote_url = tweet_url + '/quotes'
    browser.get(quote_url)
    time.sleep(3)

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        try:
            quote_list = browser.find_element(By.CSS_SELECTOR, 'div[aria-label="타임라인: 타임라인 검색"]')
            quote_each_cell = quote_list.find_elements(By.CSS_SELECTOR, 'span[class*="css-1jxf684"][class*="r-bcqeeo"][class*="r-1ttztb7"][class*="r-qvutc0"][class*="r-poiln3"]')

            for elem in quote_each_cell:
                account1 = elem.text
                if account1.startswith("@"):
                    quote_acc.add(account1)
                    print(account1)

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("더 이상 로드할 인용 계정이 없습니다.")
                break
            last_height = new_height
        except NoSuchElementException:
            print("인용 계정이 없습니다.")
            break

    # 리트윗 계정 수집
    retweet_acc = set()
    retweet_url = tweet_url + '/retweets'
    browser.get(retweet_url)
    time.sleep(3)

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        try:
            retweet_list = browser.find_element(By.CSS_SELECTOR, 'div[aria-label="타임라인: 재게시"]')
            retweet_each_cell = retweet_list.find_elements(By.CSS_SELECTOR, 'span[class*="css-1jxf684"][class*="r-bcqeeo"][class*="r-1ttztb7"][class*="r-qvutc0"][class*="r-poiln3"]')

            for elem in retweet_each_cell:
                account = elem.text
                if account.startswith("@"):
                    retweet_acc.add(account)
                    print(account)

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("더 이상 로드할 리트윗 계정이 없습니다.")
                break
            last_height = new_height
        except NoSuchElementException:
            print("리트윗 계정이 없습니다.")
            break

    # 트윗 작성자 계정 제거
    account_id = text_content.strip()
    if account_id in quote_acc:
        quote_acc.discard(account_id)
        print(f"계정 {account_id}가 quote_acc에서 삭제되었습니다.")

    # 특정 계정만 필터링
    filtered_quote_acc = {acc for acc in quote_acc if acc in target_accounts}
    filtered_retweet_acc = {acc for acc in retweet_acc if acc in target_accounts}

    print("현재 retweet_acc:", filtered_retweet_acc)
    print("현재 quote_acc:", filtered_quote_acc)

    # 트윗 데이터 구조 생성
    tweets_data = {
        "Account Name": account_name,
        "Account ID": text_content,
        "Tweet Text": tweet_text,
        "Quote Accounts": ", ".join(filtered_quote_acc) if filtered_quote_acc else "없음",
        "Repost Accounts": ", ".join(filtered_retweet_acc) if filtered_retweet_acc else "없음"
    }

    # 수집된 데이터 추가
    all_tweets_data.append(tweets_data)

# DataFrame으로 변환 후 CSV 파일로 저장
df = pd.DataFrame(all_tweets_data)
df.to_csv('twitter_crawling_data.csv', index=False, encoding='utf-8-sig')

print("모든 트윗 크롤링 완료 및 CSV 파일 저장 완료.")