import re # re는 문자의 정규화에 대한 라이브러리를 가지고 있음

text = "<title>지금은 문자열 연습입니다.</title>"

print(text[0:7])
print(text.find('문'))  # find함수는 지정한 문자가 있으면 문자의 위치값 반환
print(text.find('파'))  # find함수는 지정한 문자가 없으면 -1을 반환
print(text.index('문')) # index는 지정한 문자가 있으면 문자의 위치값 반환
# print(text.index('파')) # index는 없는 문자가 입력되면 오류 발생

text1 = "        <title>지금은 문자열 연습입니다.</title>        " # 공백이 입력되어있음
text2 = ";"
print(text1.strip()+text2) # strip()은 앞 뒤 공백을 제거해주는 함수
print(text1.lstrip()+text) # lstrip() : 왼쪽 공백만 제거
print(text1.rstrip()+text2)  # rstrip() : 오른쪽 공백만 제거
print(text1.replace('<title>', "<div>"))  # replace(a, b) : a문자열을 b로 변경시켜줌
print(text1.replace('<title>', " "))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>',text3)  # text3문자열에서 <head 뒤에 여러개의 문자가 있는 패턴을 지정해주기 위해서는 .*를 입력해줌 -> /head로 끝나는 문자열을 찾아줌
print(body)

body = body.group()  # group()이라는 함수는 텍스트만 콘솔 창에 입력됨
print(body)
print('---------------------')

text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
print(text4)
# 정규표현식
# [0-9] : 0에서 9사이의 정수를 의미, [a-z] : a에서 z사이의 소문자 알파벳을 의미
# *(0이상) +(1이상) ?(0이상 1이하)
# ab*c : b가 0이상을 의미함 (abc, abbc, abbbc, abbbbc)

# <title>지금은 문자열 연습</title>만 출력
body = re.search('<title.+/title>', text4)  # 내용이 있기 때문에 *와 +의 값이 같음.
print(body)
body = body.group()
print(body)  # <title>지금은 문자열 연습</title>

print('--------------------------------')
print(re.search('<.+>', body).group())  # <title>지금은 문자열 연습</title>, < > 안에 있는 내용을 다 search됨
print(re.search('<.+?>', body).group()) # <title> -> 하나 찾고 끝낼것 같은면 ?를 사용(반복적인 특정값을 찾고 싶으면 ?를 사용함.)

# 지금은 문자열 연습
print('----------------------------')
body = re.sub('<.+?>', '', body)  # body에서 공백을 대치해라(<.+?>을 만나면)
print(body)  

example = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2023년입니다.'
txt = re.findall(r'\d.+년', example) # 'r' : 문자열 취급해라 '\d' : 정수(숫자) / . : 숫자를 포함한 문자 / + : 1이상 / 숫자를 찾고 제일 끝에 있는 '년'을 찾음
print(txt) # ['91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2023년']
txt2 = re.findall(r'\d.+?년', example)  # findall() : 리스트형태로 반환해줌
print(txt2)