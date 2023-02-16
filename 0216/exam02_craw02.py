from bs4 import BeautifulSoup
import re  

html="""
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)


# https://example.com/fuga 찾기
# https://example.com/foo 찾기

# 패턴을 사용해서 https를 가지는 값들을 추출할 것임
lis = soup.find_all(href=re.compile(r'^https://'))  # ^: 시작 -> https://로 시작하는 패턴을 찾아라
print(lis)

for e in lis:
    print(e.attrs['href'])  # href속성만 출력
       
