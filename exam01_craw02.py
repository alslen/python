from bs4 import BeautifulSoup  # 문서를 가져와서 특정문자열을 뽑기 위해 사용
import urllib.request as req  # request와 urllib.request은 웹페이지에 접근할 수 있게 만드는 라이브러리

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
resp = req.urlopen(url) # url을 연결 시켜줌
print(resp)   # 접속했던 객체가 출력됨

soup = BeautifulSoup(resp, 'html.parser')  # url에 들어있는 내용을 파싱시켜줌
# print(soup)  # 객체값이 출력되는 것이 아니라 url에 들어있던 내용이 출력됨

# title
title = soup.find('title').string
print(title)

# wf 출력
print(soup.find('wf').string)

