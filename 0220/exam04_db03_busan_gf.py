import pymysql  # DB를 사용하기 위해 import함
import matplotlib as mpl  # 그래프 크기, 폰트 크기 지정하는 라이브러리
import matplotlib.pyplot as plt

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

# 1. DB 연결
# db = '스키마이름'
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='big9_db', charset='utf8',
                        use_unicode=True)

# 부산 날씨(날짜에 대한 최저기온과 최고기온)를 그래프로 생성
select_data = "select * from forecast where city='부산'"
cur = conn.cursor()
cur.execute(select_data)
result_busan = cur.fetchall()

min=[]  # 최저 기온
max=[]  # 최고 기온
date = []  # 날짜
for i in result_busan:
    min.append(int(i[4]))
    max.append(int(i[5]))
    # date.append(i[2])
    date.append(i[2].split('-')[2])
    # 12:00인 것만 그래프에 그리기 위해 사용
    # if i[2].split(" ")[1] == '12:00':
    #     min.append(int(i[5]))
    #     max.append(int(i[4]))
    #     date.append(i[2])

# 폰트 지정(한글을 사용하기 위해 지정)
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 그래프
plt.figure(figsize=(10,6))  # 크기
plt.plot(date, min, label='최저기온')  # plot(x좌표, y좌표)
plt.plot(date, max, label='최고기온')
plt.title('2023/2/23 ~ 2023/3/2 부산 최고 최저 기온')
plt.legend()

plt.show()

# 날씨 정보와 날씨 정보 개수를 알기 위해서 group by를 사용
select_data1 = "select wf, count(*) from forecast where city='부산' group by wf"
cur.execute(select_data1)
result_wf = cur.fetchall()
wfData = []
wfDataCount = []
for i in result_wf:
    wfData.append(i[0])
    wfDataCount.append(i[1])

plt.bar(wfData, wfDataCount, color='green')
plt.title('부산 날씨 정보')
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(wfDataCount, labels=wfData, autopct='%.1f%%')
plt.show()


##### 내가 짠 코드 #####
# # wf(구름많음, 흐림, 맑음)에 대한 막대 그래프와 원형 그래프 생성
# select_wf = 'select wf from forecast where city="부산"'
# cur.execute(select_wf)
# result_wf = cur.fetchall()
# # print(result_wf)

# wf_dic = {'구름많음' : 0, '흐림' : 0, '맑음' : 0}
# for i in result_wf:
#     if i[0] == '구름많음':
#         wf_dic['구름많음'] += 1
#     elif i[0] == '흐림':
#         wf_dic['흐림'] += 1
#     elif i[0] == '맑음':
#         wf_dic['맑음'] += 1
# print(wf_dic)

# # 막대 그래프 
# plt.bar(wf_dic.keys(), wf_dic.values())  
# plt.show()

# # 원형 그래프
# figure = plt.figure()
# axes = figure.add_subplot(111)
# axes.pie(wf_dic.values(), labels=wf_dic.keys(), autopct='%.1f%%')
# plt.show()










