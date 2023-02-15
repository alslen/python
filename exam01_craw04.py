from bs4 import BeautifulSoup  # 문서를 가져와서 특정문자열을 뽑기 위해 사용
import urllib.request as req

url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
# print(res)

soup = BeautifulSoup(res, 'html.parser')
#print(soup)


# 특정 사이트에서 값을 가져오기 때문에 
# f12 -> 가져오기 싶은 값 우클릭 -> copy -> copy Selector클릭 -> 태그의 위치를 복사 붙여넣기 할 수 있음.
#exchangeList > li.on > a.head.usd > div > span.value
#exchangeList > li.on > a.head.usd > div > span.blind

print('환율 : ', soup.select_one('span.value').string)  
print(soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string)
print(soup.select_one('div.head_info> span.blind').string)

value=soup.select('#exchangeList > li > a.head.usd > div > span.value')
print('환율 value : ', value[0].string)

blind=soup.select('#exchangeList > li > a.head.usd > div > span.blind')
print('blind value : ', blind[0].string)

value1=soup.select('#exchangeList > li > a.head.usd > div > span')
print('환율 value : ', value1[0].string)
print('blind value : ', value1[3].string)  # span영역의 3번쨰에 값이 들어 있기 때문에

