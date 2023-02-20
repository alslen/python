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

# DB에 값 insert하기위한 질의문
insert_weather = "insert into forecast(city, tmef, wf, tmn, tmx) values(%s,%s,%s,%s,%s)" # 문자열의 값을 insert하기 위해 %s를 사용


# DB에 값 추가하기 위해 크롤링을 함
req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('location'))

# DB에 있는 값은 더 이상 추가하지 못하도록 하기 위해 select 먼저 실행
select_data = "select tmef from forecast order by tmef desc limit 1"  # 내림차순 정렬해서 첫번째 값만 가져옴
cur = conn.cursor()
cur.execute(select_data)
# select한 결과를 가져오기 위해 사용하는 메서드 : fetchone()(한개의 값만 가져옴), fetchall()(여러개의 값을 가져옴)
last_date = cur.fetchone()  # db에 있는 최신날짜
print("type(last_date) : ", type(last_date))
print("last_date : ", last_date)

weather = {}
for i in soup.find_all('location'):
    weather[i.find('city').text] = []  # dic은 키 값으로 value값을 출력해줌
    for j in i.find_all('data'):
        tmp = []
        # select할 값이 없거나 최신날짜를 가진 데이터면 append시킴
        if (last_date is None) or (last_date[0] < j.find('tmef').text):  # 크롤링한 날짜가 최신 날짜이면 append시킴()
            tmp.append(j.find('tmef').text)  # 화면상에서는 tmEf로 보이지만 실제로는 tmef로 사용되었음
            tmp.append(j.find('wf').text)
            tmp.append(j.find('tmn').text)
            tmp.append(j.find('tmx').text)
            # print(tmp)
            weather[i.find('city').text].append(tmp)

print(weather)
 # 1. 연결 : connect
 # 2. 데이터베이스 작업을 위한 객체 cursor()
 # 3. 질의문 전달 : execute()
 # 4. 실행 : commit()

# dict에 있는 내용을 forecast 테이블에 저장
for i in weather:
    for j in weather[i]:
       cur = conn.cursor() # cursor 객체 생성
       cur.execute(insert_weather, (i, j[0], j[1], j[2],j[3]))  # insert할 때 어떤 값을 insert할지 명시해줘야함.
       conn.commit()  

