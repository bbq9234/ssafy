# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행합니다.
driver = webdriver.Chrome('C:/Users/student/AppData/Local/Programs/Python/chromedriver.exe')

# www.google.com으로 이동합니다.
driver.get("http://www.google.com")
time.sleep(2)

# html element 이름이 q인 것을 찾습니다. (검색창)
inputElement = driver.find_element_by_name("q")
time.sleep(2)

# 검색창에 'www.ngle.co.kr'을 입력합니다.
inputElement.send_keys("www.ngle.co.kr")
time.sleep(2)

# 검색 내용을 보냅니다.
inputElement.submit()
time.sleep(2)

# 검색된 리스트 중 링크 텍스트에 'THE BEST BUSINESS PLAN'이 포함된 것을 찾습니다.
continue_link = driver.find_element_by_partial_link_text('THE BEST BUSINESS PLAN')
time.sleep(2)

# 해당 링크를 클릭합니다.
continue_link.click()
time.sleep(5)

# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()