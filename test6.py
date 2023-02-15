import re
import codecs

# 값을 축출할 파일을 읽어와야함
f = codecs.open('friends101.txt', 'r', encoding='utf-8')  # open() 함수를 호출 할 때 " 파일 이름 "과 " 모드 "를 인자로 전달하며, 결과 값으로는 파일 객체를 반환함.
script101 = f.read()  # 파일 읽기를 수행
print(script101[:100]) # 100글자를 출력해줌

# Monica: 대사 3개 출력
lines = re.findall(r'Monica:.+', script101)  # findall은 리스트 객체로 반환해줌
print(lines[:3]) # Monica의 3개의 대사가 보이게 만들기 위해 사용
print(type(lines)) # type() : 자료구조의 유형

# All : 대사 출력
all = re.findall(r'All:.+', script101) # All:로 시작하는 모든 대사를 추출해줌.
print(all)

# All의 마지막 대사
print(all[-1])
print(len(all)) # all의 길이(리스트의 길이)

print("==========================")
# compile을 이용해 패턴을 정의해 줄 수 있음.
patt = re.compile(r'[A-Z][a-z]+:') # 첫글자 대문자 / 두번째는 소문자 / 세번째 글자부터는 소문자 하나 이상
print(re.findall(patt, script101))

print("==============================")
a = [1,2,3,4,5,2,2]
print(a)
print(set(a)) # set : 중복을 허용하지 않음

# 등장인물 출력, set : 중복 허용x
print(set(re.findall(patt, script101)))
y = set(re.findall(patt, script101))
print(type(y))

# y를 리스트 lst로 변환
lst = list(y)
print(type(lst))
print(lst)

# : 제거
print("***********")

character = []  # <class 'list'>
for i in lst:
    character += [i[:-1]] # i를 입력하면 문자 하나하나가 들어감 / [i]를 사용하면 리스트에 들어있는 문자열 자체값이 들어감
print('character : ', character)

# for i in lst:
#     print(i)

# sub 사용
character2 = []
for i in lst:
    charact = re.sub(":", '', i)
    print(charact, end=" ")  # 문자열을 출력해줌
    character2.append(charact)
    character2 += charact  # 문자 하나하나가 character2에 들어감.
###########################
print()
print(character2) # 리스트 형식으로 추가
print()

# 지문 출력
# 대소문자로 시작하고 .)으로 끝남
# \. : 마침표를 말함.
# \) : 괄호를 표현하기 위해 이스케이프 문자를 사용해서 표현
txt = re.findall(r'\([A-Za-z].+\.\)', script101)[:6]  # 찾은 값 중에 6개만 출력해주기 위해 [:6]을 사용(findall이 리스트 형이기 때문에)
print(">> txt : ", txt)
print(">> txt 길이 : ", len(txt))

# [a-z|\.] : a-z)로 끝나거나 .)으로 끝나는 것 출력 (한줄에 괄호가 여러개 입력되어있다면 제일 끝에 있는 괄호까지 찾아줌)
txt1 = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6]
print(">> txt1 : ", txt1)
print(">> txt1 길이 : ", len(txt1))

# ?는 근처에 있는 )를 찾아줌
txt2 = re.findall(r'\([A-Za-z].+?[a-z|\.]\)', script101)
print(">> txt2 : ", txt2)
print(">> txt2 길이 : ", len(txt2))
#########################################

# sub 이용해서 :(콜론) 제거
ch = 'Scene:'
ch = re.sub(":","", ch)
print(ch)

###########################################

a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
# 메일 주소만 출력
a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print('메일주소 : ', a1)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력
mm = []
for i in words:
    mm += re.findall(r'a[a-z]+', i)  # findall은 중간에 있는 a도 찾아줌
print('a로 시작하는 단어 : ', mm)
print()

for i in words:
    m = re.search(r'a[a-z]+', i)  # search도 중간에 있는 a값도 찾아서 출력해줌
    if m:
        print(m.group())
#print('search : ', m)

for i in words:
    # \d : 숫자 \D : 숫자가 아닌 것이 올때 사용
    m = re.match(r'a\D+', i)  # match는 첫단어가 a인 단어를 찾아줌(group을 사용하지 않으면 객체 값이 반환됨)
    if m:
        print("match : ", m.group())
# print('match : ', m)