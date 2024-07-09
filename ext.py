from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()
selenium_ide_path = os.path.join(os.path.curdir, 'Selenium IDE 3.17.2.0.crx')
chrome_options.add_extension(selenium_ide_path)  # 확장 프로그램 파일 경로로 변경

# ChromeDriver 설정 및 Chrome 브라우저 실행
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 브라우저 열기
project_name = 'test'
base_url = 'https://naver.com'
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
time.sleep(1)

