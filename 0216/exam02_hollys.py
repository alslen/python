import requests
from bs4 import BeautifulSoup
import pandas as pd

# 한 페이지에 대한 10개의 값을 크롤링
req = requests.get('https://www.hollys.co.kr/store/korea/korStore.do')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

tag_tbody = soup.select_one('tbody')
# print(lis)

coffee_store = []
for store in tag_tbody.select('tr'):
    store_td = store.select('td')
    store_sido = store_td[0].string
    store_name = store_td[1].string
    store_address = store_td[3].string
    store_phone = store_td[-1].string
    coffee_store.append([store_sido,store_name,store_address,store_phone])
print(coffee_store)

hollys_df = pd.DataFrame(coffee_store, columns=('지역','매장명','주소','전화번호'))
print(hollys_df)

# 페이지 번호 추가해서 출력
print('=================================')
coffee_store2 = []
for page in range(1,6):
    url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page # 뒤에 % page를 입력하면 %d에 값이 저절로 들어감
    #print(url)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_tbody = soup.select_one('tbody')

    for store in tag_tbody.select('tr'):
        store_td = store.select('td')
        store_sido = store_td[0].string
        store_name = store_td[1].string
        store_address = store_td[3].string
        store_phone = store_td[-1].string
        coffee_store2.append([store_sido,store_name,store_address,store_phone])

hollys_df2 = pd.DataFrame(coffee_store2, columns=('지역','매장명','주소','전화번호'))
print(hollys_df2)


########################################
# 함수형태로 변경(페이지 번호 추가해서 출력)
print('**************************')

def hollys_store(result) :
    for page in range(1,6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page # 뒤에 % page를 입력하면 %d에 값이 저절로 들어감
        #print(url)
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_tbody = soup.select_one('tbody')

        for store in tag_tbody.select('tr'):
            store_td = store.select('td')
            store_sido = store_td[0].string
            store_name = store_td[1].string
            store_address = store_td[3].string
            store_phone = store_td[-1].string
            result.append([store_sido,store_name,store_address,store_phone])  # 2. 전달 받은 result에 append해줌
    return result

result = []
print('-- Hollys store crawling >>>>>>>>>>>>>>>>')
hollys_store(result)  # 1. 빈 리스트를 전달 
print(result) # 들어간 내용이 출력된다.

result_df = pd.DataFrame(result, columns=('area','store','address','phone'))
print(result_df)

    
