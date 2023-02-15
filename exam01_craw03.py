from bs4 import BeautifulSoup  # 문서를 가져와서 특정문자열을 뽑기 위해 사용

html = """
    <html><body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')  # 파싱 작업
h1 = soup.find('h1').string  # h1태그를 찾아서 h1에 저장
print(h1)

h1_1 = soup.select_one('h1').string 
print(h1_1)

h1_2 = soup.select_one('div > h1').string  # div 아래에 있는 h1에 접근하기 위해 'div > h1' 사용
print(h1_2)

h1_3 = soup.select_one('div#meigen > h1').string  # div의 id='meigen'밑에 h1에 접근하기 위해 div#meigen > h1 사용
print(h1_3)

# 위에서 태그를 타고 내려올때 
li_list = soup.select('div#meigen > ul.items > li')  # 여러값이 반환되기 때문에 list형식으로 반환됨 / 여러개의 값이 오기 때문에 string사용x
print(li_list)
print(type(li_list))  # <class 'bs4.element.ResultSet'>
for i in li_list:
    print(i.string)

lis = soup.select('li')
print(lis)
for i in lis:
    print(i.string)