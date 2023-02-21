import requests
from bs4 import BeautifulSoup
import pymysql

# title, grade, reserve insert하기
dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'

# DB연결
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
use_unicode=True)  # use_unicode : 인코딩 사용 여부

insert_movie = 'insert into daum_movie(title, grade, reserve) values (%s,%s,%s)'

# 크롤링
req = requests.get("https://movie.daum.net/ranking/reservation")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

ols = soup.find('ol', class_='list_movieranking')
rankcount =  ols.find_all('div', class_='thumb_cont')
print(len(rankcount))

cur = conn.cursor() # cursor 객체 생성
for i in rankcount:
    movieTitle = i.find('a', class_='link_txt').get_text()
    movieGrade = i.find('span', class_='txt_grade').get_text()
    movieReserve = i.find('span', {'class':'txt_num'}).get_text()
    # movieReserve = i.find('span', class_='txt_num').get_text()
    print(movieTitle,movieGrade,movieReserve)
    cur.execute(insert_movie, (movieTitle,movieGrade,movieReserve))  # sql실행하기 위해 사용(execute())
    conn.commit()

# 내가 작성한 코드
# movie_div = soup.select_one('#mainContent > div > div.box_ranking > ol')
# movie_li = movie_div.select('li')
# movie_list = []
# for i in movie_li:
#     title = i.select_one('div > div.thumb_cont > strong > a').text  # 영화 제목
#     grade = i.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').text # 평점
#     reserve = i.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(2) > span').text # 예매율
#     movie_list.append([title, grade, reserve])
# print(movie_list)

# DB에 값 insert
# for i in movie_list:
#     # print(i[1])
#     cur = conn.cursor()
#     # grade_float = float(i[1])
#     cur.execute(insert_movie, (i[0],i[1],i[2]))
#     conn.commit()
