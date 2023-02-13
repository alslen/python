# 함수
# 함수를 선언하기 위해 사용하는 키워드는 def
# def seperate() :
#     a = int(input("수 입력 "))  # input은 값을 하나 받아옴 /  int() : 정수형으로 변경 / 값을 하나 받아서 정수형으로 변경 시킨 후 a에 대입
#     if a%2 == 0: 
#         print("짝수")
#     else:
#         print('홀수')


# seperate()  # 함수를 실행하기 위해 호출

# 두 수를 더하는 함수
def addReturn(a,b):
    return a+b
    
print(addReturn(3,5)) 
ret = addReturn(13,15)
print(ret)