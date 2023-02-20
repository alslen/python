import requests
from bs4 import BeautifulSoup
import pymysql  # DB를 사용하기 위해 import함

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

# 1. DB 연결
# db = '스키마이름'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
                        use_unicode=True)

# 부산의 날씨만 추출
# select_busan = 'select * from forecast where city like "%부산%"'
select_data = "select * from forecast where city='부산' order by tmef desc"
cur = conn.cursor()  # cursor 객체 생성
cur.execute(select_data)  # 질의문
result_busan = cur.fetchall()
print(result_busan)

# 부산의 최저기온, 최고기온(내가 한 코드)
select_temp = "select min(tmn), max(tmx) from forecast where city='부산'"
cur.execute(select_temp)
result_busanTemp = cur.fetchone()
print("부산 최저기온 : ", result_busanTemp[0])
print("부산 최고기온 : ", result_busanTemp[1])

#############################
print('######')
result = []
for i in result_busan:  # 부산 날씨
    # print(i)
    result.append([i[2],i[4],i[5]])
print(result)





