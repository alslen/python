import requests
from bs4 import BeautifulSoup
import re

res = requests.get('http://media.daum.net/economic/')
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)

links = soup.select('a[href]')  # a태그 중에 href속성을 갖고 있는 것들을 검색
# print(links)
# print(type(links))  # <class 'bs4.element.ResultSet'>

#100개 중 https://v.로 시작하는 기사 출력
for i in links[:100]:  # links에서 100개만 for문을 돌림

        # \w : 영문자 숫자 언더바(_) 다 올 수 있음([A-Za-z0-9_]와 같음) 
         # href속성에서 주어진 패턴을 찾아라
        # if re.search('https://v.\w+', i['href']):  
        #         print(i.get_text().strip())  # strip() : 공백 제거  / get_text()는 보여주는 것이 string보다 많음 -> 있는 거 다보여줌.
        if re.match('https://v.\w+', i['href']):  
                print(i.string)  # strip() : 공백 제거  / string은 문자열만을 보여주기 때문에 None이 나옴



# 내가 쓴 코드(몇 개는 None이라는 결과가 나옴ㅠㅠㅠ)
# lis = soup.find_all(href=re.compile(r'^https://v.'))

# for article in lis:
#         print(article.string)



