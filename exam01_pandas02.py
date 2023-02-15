import pandas as pd

# year  sales
# 2018  350
# 2019  400
# 2020  1050
# 2021  2000
# 2022  1000

data_dic = {  # DataFrame으로 변경하기 위해 dictionary형태로 먼저 선언
    "year": [2018,2019,2020,2021,2022],
    "sales": [350,400,1050,2000,1000]
}

print(data_dic)
print(type(data_dic))

df = pd.DataFrame(data_dic)  # DataFrame() : 데이터프레임 형색으로 변경시켜줌
print(df)
print(type(df))

df2 = pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]],
                    index=['중간고사', '기말고사'],   # index : 행의 이름을 지정할 있음(여려개의 값이 들어가기 위해서 []를 사용)
                    columns=['1반','2반','3반']  # columns : 열의 이름을 지정할 수 있음
)
print(df2)

df3 = pd.DataFrame([[20231101,'Kim', 90, 80],[20231102,'Lee', 80, 70],
                    [20231103,'Park', 70, 75],[20231104,'Han', 50, 60]],
                    columns=['학번','이름','중간고사','기말고사']
                    )

print(df3)
print(df3.sum())  # DataFrame의 sum() : 모든 컬럼의 값을 합쳐줌
print("중간고사 합계 : ",df3.중간고사.sum()) # 중간고사 합계
print("기말고사 합계 : ",df3.기말고사.sum()) # 기말고사 합계

# 총점 추가
df3['총점'] = df3.중간고사 + df3.기말고사
print('**********************')
print(df3)
print(df3.mean())  # 평균을 구하는 함수
print('시험평균 : ', df3.총점.mean())
print('*-------------------------*')

df4 =  pd.DataFrame([[20231101,'Kim', 90, 80],[20231102,'Lee', 80, 70],
                    [20231103,'Park', 70, 75],[20231104,'Han', 50, 60]]
                    )
print(df4)
df4.columns = ['학번','이름','중간고사','기말고사']
print(df4)
print(df4.tail())   # tail() : 끝에서 부터 5개 출력
print(df4.tail(2))

# 파일 내보내기
df3.to_csv('exam01_pandas02.csv')  # to_csv() : DataFrame형태의 값을 파일을 내보내게 하는 함수
df33 = pd.read_csv('exam01_pandas02.csv')
print(df33)

df3.to_csv('exam01_pandas020.csv', header=False)  
df333 = pd.read_csv('exam01_pandas020.csv', encoding='utf-8')
print(df333)