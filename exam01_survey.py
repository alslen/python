import pandas as pd

# servey.csv 위에서 5개 출력
df = pd.read_csv('survey.csv', encoding='utf-8')
print(df.head())  

# 평균
print(df.mean())
# 수입 합계
print('수입 합계 : ', df.income.sum())
# 수입 중앙값
print('수입 중앙값 : ', df.income.median())
print(df.describe()) # 대략적인 통계치를 알려주는 함수(describe())
print(df.income.describe())
print(df.sex.value_counts()) # value_counts() : value(값)에 대한 개수를 알려줌