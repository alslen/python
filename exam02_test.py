# 1. 1~10까지의 합 출력

sum=0
for i in range(1,11):
    sum +=i
print("1~10까지의 합 : ", sum)
print()

# 2. 구구단 출력(2단 ~ 9단)

for i in range(2,10):
    print("---",i,"단---")
    for j in range(1,10):
        print(i," * ", j, "=", i*j)
    print()

# 3. 년도만 출력
import re
exam = "저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2023년입니다."
# year = re.findall(r'\d+년', exam)
# year = re.findall(r'\d.+년', exam)  # .은 숫자를 포함한 모든 문자를 지칭함
year = re.findall(r'\d.+?년', exam)
print(year)

# 4. .으로 구분하여 문장 출력
d = 'I have a dog. I am not a girl. Yoi are not alone. I am happy'
str = re.split('\.', d)  # split() : 특정 문자로 구분하기 위해 사용
print(str)

str2 = d.split('.')  # 문자열 자체가 가지고 있는 함수를 사용한 것임,
print(str2)

# 5. 
txt = "Phoebe: Just, 'cause, I don't want her to go through what I went through with Carl- oh!"
txt += "Monica: Okay, everybody relax."
txt += "This is not even a date."
txt += "It's just two people going out to dinner and- not having sex."
txt += "Chandler: Sounds like a date to me."
txt += "Chandler: Alright, so I'm back in high school, I'm standing in the middle of the cafeteria, and I realize I am totally naked."

# 등장인물 출력
m = re.findall(r'[A-Z][a-z]+:', txt)
print(m)

# 등장인물 중복 제거하고 출력
print(set(m))

# 6_1. 문자열에서 무작위로 추출하여 새로운 변수 pw에 하나씩 병합
import random
pw = ''
# pw = str() # 문자열을 만들어주는 함수 : str()
chars = '한글우수'
for _ in range(5):  # _ : 아무 의미 없는 변수를 말함.
    pw = pw + random.choice(chars)
print(pw)


# 6. animal 리스트에서 새가 저정되어 있는 위치(인덱스만) 저장하는 리스트(이거 못함)
bird_pos = []
animals = ['새','코끼리','강아지','새','강아지','새']

# for i in range(len(animals)):  # for i in 6 -> 범위가 들어가야하기 때문에 range()를 사용
#     # print(i)
#     if animals[i] =='새':
#         bird_pos.append(i)

for i, animal in enumerate(animals): # enumerate() : 인덱스(index)와 원소를 동시에 접근하면서 for문을 돌릴 수 있음.
    print(i, ":", animal)
    if animal == '새':
        bird_pos.append(i)
print(bird_pos)

# 4부터 animals끝까지 첫번째 만나는 새의 위치값
# bird_pos.append(animals.index('새',4,len(animals)))   # index('찾고자하는 값', '시작점', '마자믹(리스트의 길이)')
# print(bird_pos)

# 7. mylist에서 짝수만 출력
mylist = [3,5,4,9,2,8,2,1]
new_list=[]

# for i in mylist:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)

# 리스트 함축 : for문과 if 조건식을 함축적으로 결합한 형식
# [i for i in 리스트명 if 조건식]   
new_list2 = [i for i in mylist if i%2==0] # mylist를 반복하면서 조건식에 맞는 값이 new_list2에 저장됨.
print('>>> ', new_list2)
print('>>> type ',type(new_list2))