from selenium import webdriver as wd  
from selenium.webdriver.common.by import By   # 

path = 'D:\\chromedriver_win32\\chromedriver.exe'  # 내가 작업하는 경로에 있는 것이 아니기 때문에 chromedriver의 위치를 잡아줘야함.
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.naver.com/') # 네이버(url)에 접속

# 파이썬을 입력해서 검색해줘
# id가 query인 해당 요소를 찾아라(driver.find_element(By.ID,'query'))
driver.find_element(By.ID,'query').send_keys('파이썬')   # 태그에서 id가 query인 것을 찾아서 '파이썬'을 입력해라
driver.find_element(By.ID, 'search_btn').click() # 태그에서 id가 search_btn인 것을 찾아서 클릭해라




