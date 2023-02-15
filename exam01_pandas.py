import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949', thousands=',')

# 면적이 200보다 큰 거 출력
print(df[df.면적>200])  # 있는 컬럼들 다 출력
print(df.loc[:,['시군구','면적']][df.면적>200]) # 시군구,면적만 출력

# 지역에 강릉이 들어간 자료만 출력
# 문자열에서 사용하는 find() : 위치값을 알려주는 함수(없으면 -1을 출력)
# print(df[df.시군구.str.find('강릉')>-1])
df_area = df[df.시군구.str.find('강릉')>-1]
print(type(df_area)) # pandas.core.frame.DataFrame
print(df_area)

# 지역이 강릉인 시군구, 가격, 면적 10행 출력
# print(df.loc[:10,['시군구', '가격', '면적']])  # loc([행, [컬럼명]]) loc([시작할 첫행:출력할 마지막 행수], [컬럼명])
print(df_area.loc[:10,['시군구', '가격', '면적']]) # 시군구가 강릉인 것 들중에서 10행을 뽑아낸다.
print(df_area.loc[:10,('시군구', '가격', '면적')])

# 면적이 130 넘는 아파트의 가격 출력
print(df.loc[:,["가격"]][df.면적>130])
print(df.가격[df.면적>130])

# 면적이 130이 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) & (df.가격<20000)])   # &를 사용하기 위해 조건 각각을 ()로 묶어줘야함.

# 면적이 130이 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) | (df.가격<20000)])

 # sort_values() : 지정한 값(by="가격)에 대한 정렬을 해주는 함수
dfAsc = df.sort_values(by="가격", ascending=False) # 가격을 기준으로 내림차순으로 정렬
print(dfAsc.가격)

print("*"*20)  # *을 20개 출력해줌
print(df.sort_values(by="가격", ascending=False).가격)

# df.loc[원하는 행 조건, 원하는 열의 조건]
# 9억원을 초과하는 가격으로 거래된 단지명(아파트), 가격 출력
print(df.loc[:, ['단지명','가격']][df.가격>90000])

# 단가 = 가격 / 면적
# df.단가 df['단가']은 같지만 없는 컬럼을 생성할 때는 df['단가']만 가능 -> 생성한 이후는 df.단가 사용 가능
df['단가'] = df.가격 / df.면적
print(df.loc[:10, ('시군구','면적','단가')])
print(df.단가)
