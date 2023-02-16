from bs4 import BeautifulSoup

fp = open('fruits-vegetables.html', encoding='utf-8')  # 파일을 열어줌
print(fp)  # 파일 객체가 출력됨

soup = BeautifulSoup(fp, 'html.parser')
print(soup)  
print()

# 파프리카 출력
print(soup.select_one('ul#ve-list > li[data-lo="us"]').string)  # 속성 값을 []에서 줌 -> 첫번째 만나는 것만 출력됨
print(soup.select('ul#ve-list > li[data-lo="us"]')[0].string)
print(soup.select_one('#ve-list > li.red').string)
# print(soup.select_one("li:nth-of-type(6)").string)  # li:nth-of-type(6): li 중에서 6번째 있는 값을 말함 -> 오류가 남, ul태그가 감싸져 있기 때문에 6번째 li를 못찾음.

# 아보카도 출력
print('-------------------------------------------------')
print(soup.select('ul#ve-list > li[data-lo="us"]')[1].string)
print(soup.select_one('#ve-list>li:nth-of-type(4)').string)
#print(soup.select_one('li:nth-of-type(8)').string)

conditon = {'data-lo' : 'us', 'class' : 'black'}
print(soup.find("li", conditon).string)  # li에서 conditon을 찾아서 문자열로 변경시켜줌
print(soup.find(id="ve-list").find("li", conditon).string)  # id가 ve-list 밑에 있는 li중에 조건이 conditon인 것을 찾아라