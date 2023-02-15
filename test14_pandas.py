import pandas as pd

data = {
    'name': ['Mark', 'Jane', 'aaa','rr'],
    'age': [33,44,55,11],
    'score': [91.2,88.5,55.6,88.9]
}

df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum()) # 합계를 구해줌(문자열은 연결됨)
print(df.mean())  # mean() : 평균값을 구해줌(구할 수 있는 것만 나타내줌)
print(df.age)  # DataFrame의 특정 속성을 뽑아줌(age속성을 뽑아줌)
print(df['age'])