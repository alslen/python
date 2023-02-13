print('Hello')

a = 0 # 파이썬은 특별히 자료형을 선언하지 않아도 됨
print(a)
print(type(a)) # type : 변수 자료형을 알 수 있음

b = 'Hello World'
print(b)
print(type(b)) # b의 유형은 str(파이썬에서 문자열을 이렇게 표현)

c = "'안녕하세요'" # 홑따옴표까지 출력가능
print(c)

d = "\'안녕하세요\'" # 자바에서는 이스케이프문자를 사용해서 '를 출력해줌 -> 파이썬에서도 이렇게 사용가능
print(d)

print(b+c) # 문자열을 더하는 것은 연결의 의미
print(2*3) 
print('2' * 3) # 문자 '2'의미 -> *3을 하면 3번 반복해서 출력
print(c*3) # '안녕하세요' 3번 출력

print('-----------------------')
print(b)
print(b[0])  # b의 첫번째 문자를 출력해줌
print(b[-1]) # 뒤에서 부터 첫번째 문자를 출력

e = '안녕하세요'
print(e[0]+e[1]) #안녕만 축출
print(e[0:2]) #첫번째문자에서 2개 축출(안녕)
print(e[1:3]) #두번째문자에서 2개 축출(녕하)
print(e[0:5:2]) # 두칸씩 건너뛰어져서 출력(안하요)
print(e[:])  # 시작점과 끝점을 생략하면 모든 문자 출력(안녕하세요)
print(e[2:]) # 두번째부터 끝까지 출력(하세요)
print(e[:3]) #처음부터 3번째 까지 출력(안녕하)

#list
l = list()  # 리스트 객체 l이 만들어짐(new 사용x)
print(l, type(l))  #현재 값이 없기 때문에 []로 출력

lst = [1,2,3]  # []가 리스트를 의미
print(lst, type(lst))

l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(l, type(l))
print(l[0])  # 리스트의 값을 출력할 때도 문자열 슬라이싱하는 법과 같다.
print(len(l)) # 리스트의 길이를 구해주는 함수 len

#l 리스트의 마지막 값 출력
print('마지막 : ', l[10])
print('마지막 : ', l[-1])
print('마지막 : ', l[len(l)-1]) # 리스트의 마지막 값을 구하기 위해 길이를 이용할 수 도 있음.

#l 리스트의 첫번쨰 값을 99로 수정
l[0] = 99
print(l[0]) # 리스트라는 자료구조는 값 변경 가능

l[1] = [1,2,3]
print(l) # 리스트 안에 리스트로 들어갈 수 있음

l[2] = '문자' # 문자도 리스트 안에 들어갈 수 있음 -> 특정 위치에 원하는 값이 들어갈 수 있음
print(l)

l.append(999)  # append()는 리스트에 마지막 값을 추가하기 위해 사용
print(l)

l.remove(5)  # 리스트에서 값 5를 지워줌
print(l)

# tuple
t = tuple()
print(t, type(t)) # 튜플은 ()로 표현

t1 = (1,2,3) # 초기화(튜플형)
print(t1, type(t1))
print(t1[0], t1[0:2])  # t1[0:2]은 튜플형으로 반환됨
print(t1+t1) # 튜플끼리 더하는 것은 문자열 연결과 비슷(튜플형으로 반환) # 새로운 튜플객체가 만들어짐

# t1의 첫번째 값을 5로 수정
# t1[0] = 5 # 오류 발생(튜플은 값을 수정할 수 x)
print(t1)


# dictionary(key와 value로 이루어짐)
d = dict() # 딕셔너리는 {}로 표현
print(d, type(d))

# 자바의 Map과 비슷함
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d, type(d))
print(d['a'])  # 키값을 주면 value값을 반환(1이 출력)

d['c'] = 33 # 값 수정 가능
print(d)

# print(d['d']) #키 값이 없기 때문에 오류
# 키 값만 가져오기 위해 keys를 사용(객체값이 출력됨)
d1 = d.keys
print('d1 : ', d1)
d2 = d.items  # 키-값형태를 모아둔 객체값이 출력됨
print('d2 : ', d2)

###############
d11 = d.keys()  # 리스트 형태로 키 값을 반환(딕셔너리에 들어 있는 키 값 자체를 가져와서 출력)
print('keys : ', d11, type(d11)) # 유형 'dict_keys'
d22 = d.items()  # 키-값 형태로 출력해줌(리스트형태로 반환)
print("items : ", d22, type(d22)) #유형 'dict_keys'
d33 = d.values()  # 값만 출력해줌(리스트 형태로)
print('values : ', d33, type(d33)) # 유형 'dict_keys'

print("type list", type(list(d.keys()))) # 리스트형태로 변경 -> list()안에 딕셔너리값이 들어가면 됨

dset = set(d.keys())
print(dset, type(dset))

# 조건문
a = 2
if(a == 1):  # 파이썬은 조건문에 :(콜론)을 사용 -> 들여쓰기 중요(자바에서 {}역할을 파이썬에서는 들여쓰기로 표현)
    print(1)
else:
    print("1아님")

if(a==1):
    print(1)
elif(a==2):  # 파이썬에서는 elif를 사용(else if역할을 elif가 대신 사용)
    print(2)
else:
    print(3)

print('-----------------------')

# 반복문(파이썬은 반복문에도 :(콜론)을 사용)
for i in [1,2,3]:  # 1 2 3 차례로 i에 들어감
    print(i)

for i in (1,2,3):
    print(i)

for i in "Hello": # H e l l o 차례로 i에 들어가서 출력됨
    print(i)

num = 5 # 초기값 셋팅
while(num>0):
    print(num)
    num -= 1

print('---while---')
num = 10
while(num>0):
    if(num==6):
        print('---end---')
        break # 반복문 탈출
    print(num, end=' ') # 가로로 출력(공백을 주어서 구분)
    num -= 1

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=" ")  # 공백으로 구분
print() # 개행

for i in range(10):  # range(10) : 0~9까지 의미(범위를 지정할 때 사용)
    print(i, end=" ")
print()

# 100까지 수 중에 7의 배수의 합계 출력
print("---7의 배수---")
sum = 0
for i in range(100):
    if(i%7==0):
        sum += i
        print(i, end=" ")  # 들여쓰기 중요~!!!(if문에 걸려야하기 때문에)
print("\nsum : ",sum) # \n을 사용하면 개행 가능(java와 같음)

# * * *
# * * *
# * * *
print("---star---")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print("")

d1 = {
    'a':1,
    'b':2,
    'c':3
}
 
print('--------------------')
value_max = max(d1.values())  # 최대값을 구하기 위해 max를 사용
print("max : ", value_max)

# key : a  value : 1 ...
for k, v in d1.items():  # 반복문에서 값을 받는 변수를 2개 선언 가능(k는 key값이 저장, v는 value값이 저장)
    print('key : ', k, ' value : ', v)
    if(value_max == v):
        print('key : ', k)  # max key값이 출력

