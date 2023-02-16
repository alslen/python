import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 이름(지역), 현재 기온, 습도 크롤링
table = soup.find('table', {'class':'table-col'})
# print(table)
datas = []
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) > 0:
        print('지역 = ', tds[0].text)
        print('온도 = ', tds[5].text)
        print('습도 = ', tds[-4].text)
        print()
        datas.append([tds[0].text,tds[5].text,tds[-4].text])

print(datas)

# 읽어온 값을 파일로 내보내기
df = pd.DataFrame(datas, columns=('point', 'temp', 'hum'))
df.to_csv('weather.csv', encoding='euc-kr', index=False)

# 읽어온 값을 파일로 내보내기
wdf = pd.read_csv('weather.csv', encoding='euc-kr')
print(wdf)

###########################################
with open('weather_file.csv', 'w') as file:
    print('파일저장')
    file.write('point, temp , hum\n')
    for item in datas:
        row = ','.join(item)  # ,와 item을 연결시킴(join메서드를 이용)
        file.write(row+'\n')

file_df = pd.read_csv('weather_file.csv', encoding='euc-kr')
print(file_df)

#####################################

print("##### select #####")
tbody = soup.select_one('#weather_table > tbody')
# print(table)
result = []
for tr in tbody.select('tr'):
    tds = tr.select('td')
    print('지역 = ', tds[0].text)
    print('온도 = ', tds[5].text)
    print('습도 = ', tds[-4].text)
    print()
    result.append([tds[0].text,tds[5].text,tds[-4].text])

print(result)

# # DataFrame
df = pd.DataFrame(datas, columns=('지역', '온도', '습도'))
df.to_csv('weather_select.csv', encoding='euc-kr', index=False)

sdf = pd.read_csv('weather_select.csv', encoding='euc-kr')
print(sdf)


# 내가 쓴 코드
# tbody = soup.select_one('#weather_table > tbody')
# # print(tbody.string)

# wheathers = []
# for weather in tbody.select('tr'):
#     weather_id = weather.select('td')
#     weather_sido = weather_id[0].string
#     weather_temp = weather_id[5].string
#     weather_humidity = weather_id[10].string
#     wheathers.append([weather_sido,weather_temp,weather_humidity])
#     # print("지역 = ", weather_sido)
#     # print("현재기온 = ", weather_temp)
#     # print("습도 = ", weather_humidity)
#     # print()

# # DataFrame형태로 값을 변경
# result = pd.DataFrame(wheathers, columns=('지역','현재 기온','습도'))
# #print(df)

# # DataFrame형태로 파일에 값을 쓰기 위해 to_csv를 사용
# result.to_csv('weather.csv', index=False)

# # read_csv로 weather.csv파일을 읽음.
# df = pd.read_csv('weather.csv', encoding='utf-8')
# print(df)



