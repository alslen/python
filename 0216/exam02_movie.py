import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

ol = soup.select_one('#mainContent > div > div.box_ranking > ol')
lis = ol.select("li")
# print(lis)

for i in lis:
    movieTitle = i.select_one('a.link_txt').get_text()
    movieGrade = i.select_one('span.txt_grade').get_text()
    movieReser = i.select_one('span.txt_num').get_text()
    print('영화 : ', movieTitle, end=" / ")
    print('평점 : ', movieGrade, end=" / ")
    print('예매율 : ', movieReser)

print('--------------------------------------------------')
# find 사용
movies=[]
for i in lis:
    movieTitle = i.find('a', class_='link_txt').get_text()
    movieGrade = i.find('span', 'txt_grade').get_text()
    movieReser = i.find('span',{'class':'txt_num'}).get_text()
    print('영화 : ', movieTitle, end=" / ")
    print('평점 : ', movieGrade, end=" / ")
    print('예매율 : ', movieReser)
    movies.append([movieTitle, movieGrade, movieReser])

movie_df = pd.DataFrame(movies, columns=('영화제목', '평점', '예매률'))
print(movie_df)

# for i in range(1,21):
#     i = str(i)
#     title = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > strong > a').string
#     stars = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').string
#     rate = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > span.txt_append > span:nth-child(2) > span').string
#     print("영화 : ", title, " / 평점 : ", stars, "/ 예매율 : ", rate)
