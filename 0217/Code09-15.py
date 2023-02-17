import bs4
import urllib.request
import pandas as pd

## 함수 선언 부분 ##
def getBookInfo(book_tag):
    names = book_tag.find("div", {"class":'goods_name'})
    bookName = names.find('a').text
    auths = book_tag.find('span', {'class':'goods_auth'})
    bookAuth = auths.find('a').text
    bookPub = book_tag.find('span', {'class':'goods_pub'}).text
    bookDate = book_tag.find('span', {'class':'goods_date'}).text
    bookPrice = book_tag.find('em', {'class':'yes_b'}).text
    return [bookName, bookAuth, bookPub,bookDate,bookPrice]

## 전역 변수 부분 ##
url = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="
pageNumber = 1

## 메인 코드 부분 ##
# while True:
#     try:
#         bookUrl = url+str(pageNumber)
#         pageNumber += 1

#         htmlObject = urllib.request.urlopen(bookUrl)
#         webPage = htmlObject.read()
#         bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
#         tag = bsObject.find('ul', {'class':'clearfix'})
#         all_books=tag.find_all('div', {'class' : 'goods_info'})

#         for book in all_books:
#             print(getBookInfo(book))
#     except:
#         break


# 1 페이지만 데이터를 크롤링해서 제목, 저자, 출판사, 출판일, 가격
# with open()
# yes24.csv 파일로 저장
# 그 파일을 읽어서 저장
# bookUrl = url + str(pageNumber)

# htmlObject = urllib.request.urlopen(url)
# webPage = htmlObject.read()
# bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
# tag = bsObject.find('ul', {'class':'clearfix'})
# all_books=tag.find_all('div', {'class' : 'goods_info'})

# book_list = []
# for book in all_books:
#     book_list.append(getBookInfo(book))

# print(book_list)

# with open('yes24.csv', 'w', encoding='utf-8-sig') as file:
#     file.write('제목    저자   출판사   출판일   가격\n')
#     for i in book_list:
#         row = ','.join(i)
#         file.write(row+'\n')
        

#########################################################
# 50페이지까지
# pandas 이용
# yes24_50.csv 파일로 저장
# 그 파일을 읽어서 저장

for i in range(1,50):
    try:
        bookUrl = url+str(pageNumber)
        pageNumber+=1

        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

        tag = bsObject.find('ul', {'class' : 'clearfix'})
        book_list = tag.find_all('div', {'class':'goods_info'})

        book_list2 = []
        for book in book_list:
            book_list2.append(getBookInfo(book))
    except:
        break
# print(book_list2)
