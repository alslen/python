import requests
from bs4 import BeautifulSoup

url ='https://finance.naver.com/item/main.naver?code=252670'
response = requests.get(url)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string)
print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').get_text())  # string과 get_text()가 하는 역할이 같음 -> 태그를 제외한 문자열만을 추출해줌.

# 2,810
today = soup.select_one('div > p.no_today')
price = today.select_one('span.blind')
print(price.get_text())
print(soup.select_one('#chart_area > div.rate_info > div > p.no_today > em > span.blind').string)


##################################
# [['KODEX 200선물인버스2X', '2,810'], ['KODEX 코스닥150선물인버스', '4,750']]

# url = 'https://finance.naver.com/item/main.naver?code='+252670
# url = 'https://finance.naver.com/item/main.naver?code='+251340

result = [] # 값을 담을 리스트 선언
code = ['252670','251340']  
for i in code:
    url = 'https://finance.naver.com/item/main.naver?code='+i  # 주소가 비슷하기 때문에 다른 부분을 code에 담아서 for문을 돌림
    # print(url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
    # print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string)
    today = soup.select_one('div > p.no_today')
    price = today.select_one('span.blind')
    # print(price.get_text())
    result.append([name, price.get_text()])

print(result)
    



