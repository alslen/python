# 사이트에 접속해서 특정 값을 가져오기 위해 requests를 사용
import requests

URL = 'http://www.naver.com'
response = requests.get(URL)  # URL을 연결시켜줌
print(response)

html_data = response.text # 읽어온 객체에 저장되어있는 문자열을 가저옴
# print(html_data)

print(html_data.find('<h3 class="blind">'))  # <h3 class="blind"> <- 이 값이 있는 위치값을 반환해줌(236442)
print(html_data.find('급'))