from selenium import webdriver as wd  
from selenium.webdriver.common.by import By  
import time 
import matplotlib as mpl
import matplotlib.pyplot as plt


path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos') # 드라이버를 통해 url에 접근

# all_videos = driver.find_elements(By.ID, "dismissible")  # id값이 dismissible인 모든 것(요소)을 찾음
all_videos = driver.find_elements(By.CSS_SELECTOR, "#dismissible")  # CSS_SELECTOR : css표현으로 id값(#사용)을 가져옴
print(all_videos)

time.sleep(2) #2초 기다림

# 제목, 재생시간, 조회수
datas = []
for video in all_videos:
    title = video.find_element(By.ID, "video-title").text
    video_time = video.find_element(By.CSS_SELECTOR, ".style-scope ytd-thumbnail-overlay-time-status-renderer").text.strip()  # 재생시간
    # video_num = video.find_element(By.CLASS_NAME, "inline-metadata-item style-scope ytd-video-meta-block").text.strip() # 조회수
    video_num=video.find_element(By.XPATH, ' //*[@id="metadata-line"]/span[1]').text  # XPath를 이용해서 조회수 크롤링
    datas.append([title, video_time, video_num])
print(datas)

# 조회수별로 나누기 위해 dictionary를 사용함.
youtube_dic = {'100만이상' : 0, '50만이상' : 0, '10만이상' : 0}
for item in datas:
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())
    if item >= 100:
        youtube_dic['100만이상'] += 1
    elif item >= 50:
        youtube_dic['50만이상'] += 1
    elif item >= 10:
        youtube_dic['10만이상'] += 1
print(youtube_dic)

# 그래프 그리기
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(youtube_dic.values(), labels=youtube_dic.keys(), autopct='%.1f%%')
plt.show()




 




