import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949')  # pandas는 다양한 형태의 파일을 읽어올 수 있도록 제공해줌
print(len(df))
print(type(df))
print(df.shape)  # (행,열)의 값으로 반환
print(df.head()) # head() : 데이터를 위에서 5개를 뽑아줌
print(df.tail()) # tail() : 데이터를 밑에서 5개를 뽑아줌
print('--------------------------------------')

print(df.면적)  # 면적만 찍힘
print('-------------------')
# 면적이 200 큰 거 출력
print(df[df.면적>200])
print('-------------------')

# 10개만 단지명, 가격 출력
print(df.loc[:10, ['단지명','가격']])  # loc[[행,열]]:원하는 행과 열을 뽑아주는 함수

# 단지명, 가격, 면적을 출력 단, 면적 130보다 큰거 출력
print('-----------------------------------')
print(df.loc[:,['단지명', '가격', '면적']][df.면적 > 130])
