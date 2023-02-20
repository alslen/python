from selenium import webdriver as wd  
from selenium.webdriver.common.by import By  
import time 
from selenium.webdriver.common.keys import Keys

path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://tour.interpark.com/?mbn=tour&mln=tour') # 드라이버를 통해 url에 접근

# 제주도를 검색
driver.find_element(By.ID, 'divHeaderSearch').click()
driver.find_element(By.ID, 'txtHeaderInput').send_keys('제주도')
driver.find_element(By.ID, 'btnHeaderInput').click()

# 국내 숙박부분 => 호텔명 / 가격 / 평점
hotel_ul = driver.find_element(By.CLASS_NAME, 'boxList')



    



