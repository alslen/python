from bs4 import BeautifulSoup  # 문서를 가져와서 특정문자열을 뽑기 위해 사용

# 문자열로 출력하기 위해서 """ or ''' 사용함(태그들을)
html = """
    <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
# print(html)

soup = BeautifulSoup(html, 'html.parser')  # html.parser를 이용해서 html을 해석해줌
print(soup)  # 파싱이 된 내용이 출력됨

h1 = soup.html.body.h1  # html태그 밑에 body태그 밑에 h1내용을 h1에 저장
print(h1)

p = soup.html.body.p  # 첫번째 p태그를 찾아줌
print(p)

p1 = p.next_sibling.next_sibling # next_sibling : 형제 노드를 찾아줌(p에 대한 형제노드를 찾아줌)
print(p1)

########################
print()
print("h1 string : ", h1.string)  # 태그는 빼고 문자열만 가져옴
print("h1 text : ", h1.text)  # 태그는 빼고 문자열만 가져옴
print('p : ', p.string)
print('p1 : ', p1.text)


html2 = """
    <html><body>
    <h1 id='title'>스크레이핑이란?</h1>
    <p id='body'>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
print()

# id='title'인 내용 추출
soup = BeautifulSoup(html2, 'html.parser')
title = soup.find(id='title')  # find : id가 'title'인 것을 찾음
print(title.string)

# id='body'인 내용 추출
print(soup.find(id='body').string)
