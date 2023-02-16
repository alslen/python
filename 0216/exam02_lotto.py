import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# find로 로또번호 크롤링
ballNum = soup.find_all('span', class_='ball')
for i in ballNum:
    print(i.get_text(), end="\t") # i.get_text()

# select로 로또번호 크롤링
print()
nums = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
#print(nums)
for i in nums:
    print(i.get_text(), end="\t")


# 내가 작성한 코드
# print("select로 크롤링")
# for lotto in range(8):
#     num = soup.select('#container > div > div.bx_lotto_winnum > span')
#     print(num[lotto].string, end=" ")
# print()

# print("find로 크롤링")
# for flotto in soup.find('div', {'class':'bx_lotto_winnum'}):
#     print(flotto.string, end=" ")
   