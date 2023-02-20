from selenium import webdriver as wd  
from selenium.webdriver.common.by import By  
import time 
from selenium.webdriver.common.keys import Keys


path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos') # 드라이버를 통해 url에 접근

# all_videos = driver.find_elements(By.ID, "dismissible")  # id값이 dismissible인 모든 것(요소)을 찾음
all_videos = driver.find_elements(By.CSS_SELECTOR, "#dismissible")  # CSS_SELECTOR : css표현으로 id값(#사용)을 가져옴

# selenium는 스크롤을 내려야지만 값이 들어가기 때문에 
body_tag = driver.find_element(By.TAG_NAME, 'body')
# print(body_tag) # 객체값 출력
body_tag.send_keys(Keys.END) # 스크롤이 1번 진행됨.

# 화면의 길이 만큼 스크롤을 해줘야하기 때문에 
# 화면 길이 확인하기
# document.documentElement.scrollHeight : 화면길이
print(driver.execute_script('return document.documentElement.scrollHeight'))

# 무한루프 돔ㅠㅠㅠㅠㅠ
while True:  
   last_height =  driver.execute_script('return document.documentElement.scrollHeight')  
   print('last_height : ', last_height)
   # 10번 스크롤하기
   for i in range(10):
    body_tag.send_keys(Keys.END)
    time.sleep(1) # 스크롤 할 때 데이터가 로드 되어야하기 때문에 기다림
    new_height = driver.execute_script('return document.documentElement.scrollHeight') # 스크롤 될때마다 화면길이가 달라지기 때문에 선언
    print('new_height : ', new_height)

    if last_height == new_height:
        print('화면길이 같아서 반복 종료')
        break
    print('='*100)

 




