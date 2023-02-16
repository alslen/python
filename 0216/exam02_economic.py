import requests
from bs4 import BeautifulSoup
import re
res = requests.get('http://media.daum.net/economic/')
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)

#100개 중 https://v로 시작하는 기사 출력
lis = soup.find_all(href=re.compile(r'^https://v.'))
# print(lis.select('img')['alt'])

for article in lis:
        print(article.string)

