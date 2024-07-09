from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

driver: webdriver.Chrome
download_dir = os.path.join(os.path.curdir, 'record\\')


def initialize_driver():
    global driver
    # Chrome 옵션 설정
    chrome_options = webdriver.ChromeOptions()
    selenium_ide_path = os.path.join(os.path.curdir, 'Selenium IDE 3.17.2.0.crx')
    chrome_options.add_extension(selenium_ide_path)  # 확장 프로그램 파일 경로로 변경
    chrome_options.add_argument("--start-maximized")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    chrome_options.add_experimental_option("prefs", {
        #"download.default_directory": download_dir,
        "download.default_directory": r"C:\Users\xxx\downloads\Test",
        "download.prompt_for_download": False,  # 다운로드 확인 창 비활성화
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # ChromeDriver 설정 및 Chrome 브라우저 실행
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)


def start_web_record(project_name: str, base_url: str):
    driver.get("chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(15) > div > div > div > div > div.dialog__contents > form > div.dialog__main > div > ul > li:nth-child(1) > a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div > div > div > div.dialog__contents > form > div.dialog__main > div > input[type=text]").send_keys(project_name)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div > div > div > div.dialog__contents > form > div.dialog__footer > div > span:nth-child(1) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div > div > div > div.dialog__contents > form > div.dialog__main > div > input[type=text]").send_keys(base_url)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div > div > div > div > div.dialog__contents > form > div.dialog__footer > div > span:nth-child(1) > button").click()


def keep_alive_while_record():
    while True:
        window_handle = driver.window_handles
        if len(window_handle) == 1:
            break
        time.sleep(0.5)


def save_web_record():
    driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.SplitPane.horizontal > div.Pane.horizontal.Pane1 > div > div.content > div > div.Pane.vertical.Pane1 > aside > div.tests_div.active > ul > li > div > a > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(16) > div > div > div > ul > li:nth-child(4) > a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#python-pytest").click()
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(14) > div > div > div > div > div.dialog__contents > form > div.dialog__footer > div > span:nth-child(1) > button").click()


# 파일 다운로드가 완료되었는지 확인하는 함수
def wait_for_downloads(download_dir, timeout=30):
    end_time = time.time() + timeout
    while time.time() < end_time:
        files = os.listdir(download_dir)
        if files:
            for file in files:
                if file.endswith('.crdownload'):
                    time.sleep(1)
                    break
            else:
                return True
        else:
            time.sleep(1)
    return False


initialize_driver()
start_web_record(project_name="hello", base_url="http://naver.com")
keep_alive_while_record()
save_web_record()
wait_for_downloads(download_dir)
