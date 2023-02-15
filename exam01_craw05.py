from bs4 import BeautifulSoup  # 문서를 가져와서 특정문자열을 뽑기 위해 사용
import urllib.request as req

url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# mw-content-text > div.mw-parser-output > ul:nth-child(6) : 제일 위에 있는 ul을 뽑아와야함
lst = soup.select('#mw-content-text > div.mw-parser-output > ul > li > a')
for i in lst:
    print('- ', i.string)



