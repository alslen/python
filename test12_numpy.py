# numpy : 수치 계산을 쉽게 하기 위해 사용하는 라이브러리
import numpy as np
a = np.array([[2,3],[5,2]]) # 이차원 배열 선언
print(a)

d = np.array([2,3,4,5,6]) # 일차원 배열
print(d)

print(d.shape) # shape은 일차원 배열에서는 열의 수만 알려줌
print(a.shape) # shape은 행과 열의 수를 알려줌

e = np.array([[1,2,3,4],[5,6,7,8]])
print(e.shape)
print("e.dtype>> ", e.dtype)
print(np.zeros((2,10))) # zeros((행,열)) : 입력한 행과 열만큼 0으로 배열을 채워줌
print(np.ones((2,10)))  # ones((행,열)) : 입력한 행과 열만큼 1로 배열을 채워줌
print(np.arange(2,10))  # 2이상 10미만 이루어진 일차원 배열을 생성해줌

a = np.ones((2,3))
print(a, a.shape)

b = np.transpose(a) # transpose(행과 열을 바꿔줄 값) : 행과 열을 바꿔주는 함수
print(b, b.shape)

arr1 = np.array([[1,2,3],[6,7,8]])
arr2 = np.array([[12,22,33],[16,17,18]])
# 배열 덧셈
print(arr1+arr2) # 같은 자라에 있는 원소끼리 더해짐
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

##########
d = np.array([[1,2,3,4,5,6],[2,3,4,5,6,7],[5,6,7,8,9,9]])
d_list = [[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9,9]]
# print(d.shape)
print(d)
print(d_list)
print(d_list[:2])
# d_list[:2] = 0  # 오류 발생
d[:2] = 0   # 1행, 2행 0으로 변경 
print(d)
print(type(d_list))  # <class 'list'>
print(type(d)) # <class 'numpy.ndarray'>
print('--------------------')
print(np.arange(10)) # 0~9까지 일차원 배열의 원소로 들어감

# 각각의 원소에 10을 더해줌
arr4 = np.arange(10)+10 
print(arr4)
print(arr4[-3:]) # [17 18 19]
print('-----------------------')
print(arr1)
print(arr1[1,2])  # numpy에서 행과 열은 0부터 시작 -> 8(결과값)
print(arr1[:,2])  # 2열의 모든 행을 출력
print(arr1[1,:]) # 1행의 모든 열을 출력