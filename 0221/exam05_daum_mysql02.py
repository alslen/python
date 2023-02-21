import requests
from bs4 import BeautifulSoup
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt

# grade(평점)로 원형 그래프 생성
dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
use_unicode=True)

select_movie = 'select grade from daum_movie'

cur = conn.cursor()
cur.execute(select_movie)
movies = cur.fetchall()  # select한 검색결과를 가져오기 위해 fetchall()을 사용 -> 튜플형태로 값이 출력됨
print(movies)
print(type(movies))

# 평점이 9점이상, 8점이상, 6점이상, 6점미만 ==> pie
movieDic = {'9점이상':0, '8점이상':0, '6점이상':0, '6점미만':0}
for movie in movies:
    movie = float(movie[0])
    if movie >= 9:
        movieDic['9점이상'] += 1
    elif movie >= 8:
        movieDic['8점이상'] += 1
    elif movie >= 6:
        movieDic['6점이상'] += 1
    else:
        movieDic['6점미만'] += 1
print(movieDic)

# font 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()  # font이름 먼저 설정해줘야함
mpl.rc('font', family=font_name)

figure = plt.figure()  # figure() : 그래프를 그려줌
axes = figure.add_subplot(111)  # 그래프를 여러개 추가할 수 있지만 1행 1열의 첫번째 그래프만 표시하기 위해서 111을 써줌
axes.pie(movieDic.values(), labels=movieDic.keys(), autopct='%.1f%%')  # autopct = :수치는 소수점첫째자리까지 표시하기 만들어줌
plt.show()
    


