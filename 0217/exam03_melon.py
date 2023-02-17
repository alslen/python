import requests
from bs4 import BeautifulSoup

# 멜론은 headers라는 옵션을 사용해서 내가 사용하는 값을 명시해줘야함(F12-> Newtowrk -> 아무 값 클릭 -> User-Agent에 명시 되어있음)
header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/week/index.htm', headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup)

#lst50 > td:nth-child(2) > div > span.rank : 순위
#lst50 > td:nth-of-type(6) > div > div > div.ellipsis.rank01 > span > a : 곡 제목
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a : 이름
music_list = soup.select('#lst50 > td:nth-of-type(6) > div > div > div.ellipsis.rank01 > span > a')
# print(music_list)


# 저장소에서 인덱스를 뽑아오기 위해서 enumerate 사용
# enumerate : 위치값과 데이터값을 가져올 수 있음
for idx, i in enumerate(music_list,1):  # 리스트 뒤에 1을 지정한 이유는 1부터 시작하기 만들기 위해서
    print(idx, i.text)



