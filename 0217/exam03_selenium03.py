from selenium import webdriver as wd  
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
# print(soup)

all_videos = soup.find_all(id='dismissible')  # id가 dismissible인 것에 대한 내용을 all_videos에 담아라
datas = []

# 제목, 재생시간, 조회수 값 추출
for video in all_videos:
    title = video.find(id='video-title').text  # 제목
    video_time = video.find('span', {'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).text.strip() # 재생시간
    video_num = video.find('span', {'class' : 'inline-metadata-item style-scope ytd-video-meta-block'}).text.strip() # 조회수
    # print(title, video_time, video_num)
    datas.append([title,video_time,video_num])
# print(datas)

# datas에 들어있는 값들을 파일에 내보내기
# df = pd.DataFrame(datas, columns=('제목', '재생시간', '조회수'))
# df.to_csv('yotubu.csv', encoding='utf-8-sig', index=True)

# 조회수별로 나누기 위해 dic을 사용함.
youtubu_dic = {'100만이상' : 0, '50만이상' : 0, '10만이상' : 0}
for item in datas:
    # ex> 유튜브 조회수 34만회
    # str(item).split('조회수')[1] : 34만회 -> .split('만회')[0] : 34
    item = float(str(item).split('조회수')[1].split('만회')[0].strip()) 
    if item >= 100:
        youtubu_dic['100만이상'] += 1
    elif item >= 50:
         youtubu_dic['50만이상'] += 1
    elif item >= 10:
         youtubu_dic['10만이상'] += 1
print(youtubu_dic)

# 그래프 그리기
# 한글 사용하기 위해서 한글 폰트를 가져와야함
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()  # 그림을 그릴 객체 생성
axes = figure.add_subplot(111) # subplot : 부분적인 그래프를 여러개 그릴 수 있는 함수
# pie(각 영역의 비율, labels=영역의 이름, autopct=원형그래프안에 표현될 숫자 형식)
axes.pie(youtubu_dic.values(), labels=youtubu_dic.keys(), autopct='%.1f%%')  # 파이 차트를 그려줌
plt.show()


# 내가 쓴 코드
# div = soup.select('#metadata-line')

# for i in div:
#     views = i.select_one('span:nth-child(3)').string
#     time = i.select_one('span:nth-child(4)').string


 




