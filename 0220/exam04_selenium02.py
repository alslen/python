from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# driver.get('https://google.com') # 드라이버를 통해 url에 접근
r = driver.execute_script('return 100*50') # execute_script(자바스크립트로 실행하고자 하는 것 쓰기) : 자바스크립트를 실행하기 위해 사용
print(r)