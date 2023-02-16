import requests

r = requests.get('http://api.aoikujira.com/time/get.php')  # requests는 get메소드를 통해서 url을 연결시킴
txt = r.text  # text : 텍스트형태의 데이터를 추출해줌
print(txt)

bin = r.content  # content : 바이너리 형식으로 데이터 추출
print(bin)