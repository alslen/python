from selenium import webdriver as wd  
from bs4 import BeautifulSoup
import re
import pandas as pd

path = 'D:\\chromedriver_win32\\chromedriver.exe'  # 내가 작업하는 경로에 있는 것이 아니기 때문에 chromedriver의 위치를 잡아줘야함.
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.melon.com/chart/week/index.htm') # 가상 인터넷(chromedriver)과 url을 연결시켜줌 

page = driver.page_source # driver에 위에 있는 홈페이지에 대한 값을 읽어오기
soup = BeautifulSoup(page, 'html.parser') # 읽어온 값을 BeautifulSoup을 이용해서 파싱을 해줌
# print(soup)

# 곡 제목만 출력
# music_list = soup.select('#lst50 > td:nth-of-type(6) > div > div > div.ellipsis.rank01 > span > a')
# # print(music_list)

# for idx, i in enumerate(music_list,1):
#     print(idx, i.text)

# 순위 곡정보 앨범 좋아요 수 출력(50개)
trs = soup.select('tr#lst50')
datas = []
for tr in trs:
    rank = tr.select_one('span.rank').get_text()
    name = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
    singer = tr.select_one('div.ellipsis.rank02 > span > a').get_text()
    album = tr.select_one('div.rank03 > a').get_text()
    likes = tr.select_one('span.cnt').get_text()
    likes = re.sub('\n총건수\n','', likes)   # \n총건수\n를 공백으로 만들기 위해 사용
    likes = re.sub(',','', likes)
    # print(rank, name, singer, album, likes)
    datas.append([rank, name, singer, album, likes])
print(datas)

# melon.csv (읽어온 데이터를 파일로 내보내기)
# with open : melon_file.csv
with open('melon_file.csv','w', encoding='utf-8-sig') as file:
    file.write('순위 곡명   가수    앨범    좋아요수\n')  # 젤 윗부분에 적히는 부분
    for item in datas:
        row = ','.join(item)  # ,로 구분하기 위해 사용
        file.write(row+'\n')

# pandas : melon_pandas.csv
df = pd.DataFrame(datas,columns=('순위','곡 제목','가수명','앨범','좋아요수'))
df.to_csv('melon_pandas.csv', encoding='utf-8-sig', index=False)  # index=False : 인덱스번호를 사용x
# 파일에 있는 값을 읽어옴
df = pd.read_csv('melon_pandas.csv', encoding='utf-8-sig')
print(df)



# 내가 작성한 코드
# music = soup.select('#lst50')
# chart = []
# for i in music:
#     rank = i.select_one('td:nth-child(2) > div > span.rank')
#     title = i.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
#     singer = i.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
#     album = i.select_one('td:nth-child(7) > div > div > div > a')
#     like = i.select_one('td:nth-child(8) > div > button > span.cnt')
#     like_num = re.sub("\n총건수\n",'',like.get_text())
#     chart.append([rank.string,[title.string,album.string],singer.string, like_num])
#     #print(rank.string, "", title.string, "",album.string,"", singer.string, "", like.get_text())
# #print(chart)

# df = pd.DataFrame(chart, columns=('순위', '곡정보', '앨범', '좋아요'))
# print(df)

# df.to_csv('melon.csv', index=False)