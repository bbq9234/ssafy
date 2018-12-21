import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ff_driver = webdriver.Chrome('C:/Users/student/AppData/Local/Programs/Python/chromedriver.exe')
ff_driver.get("http://www.kweather.co.kr/air/air_forecast.html")

# link = ff_driver.find_element_by_xpath('//*[@id="video-title"]')

WebDriverWait(ff_driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "briefingText_airforecast")))

page_results = ff_driver.find_element(By.CSS_SELECTOR, "briefingText_airforecast")

print(page_results.get_attribute("href"))
