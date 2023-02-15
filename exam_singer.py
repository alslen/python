import pandas as pd  # pandas : 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있음
import usecsv
import csv

# singer2.csv 읽어 [이름, 조회수] 300000 넘는 거 출력

# 내가 짠 코드
# a = [["이름", "유튜브 조회수"]]
# for i in listName:
#     try:
#         if i[-1]>300000:
#             a.append([i[1], i[-1]])
#     except:
#         pass
# print(a)

sing = usecsv.opencsv('singer2.csv')
sing_list = usecsv.switchcsv(sing)
# print(sing_list)

new_list = [['이름', '조회수']]
for i in sing_list:
    try:
        if i[6] >= 300000:
           # print(i[1], i[6])
           new_list.append([i[1],i[6]])
    except:
        pass
print(new_list)

# 파일로 내보내기 youtube30.csv
# with open('yotube30.csv','w',newline='') as yotube30:
#     a = csv.writer(yotube30)
#     a.writerows(new_list)

#################################################


# # pandas read_csv
# # 유튜브 조회수가 300000 넘는 거 출력
# pandas를 이용해 파일을 읽기 위해서 사용하는 함수 : read_csv()

# df = pd.read_csv('singer2.csv', encoding='cp949', thousands=',')
# print(df.loc[:,['이름', '유튜브 조회수']][df['유튜브 조회수'] > 300000])

df = pd.read_csv('singer2.csv', encoding='cp949', thousands=',') # thousands : 지정한 문자를 제거해줌
print(df)
print(df['유튜브 조회수'])
# print(df.유튜브 조회수)  # 이 방법 컬럼에 공백이 있으면 사용할 수 없음
# [df["유튜브 조회수"]>300000] : 값이 true, false로만 나옴 -> 값 자체를 출력해주기 위해서 loc를 사용
print(df[df['유튜브 조회수']>300000])
print(df.loc[:,['이름','유튜브 조회수']][df["유튜브 조회수"]>300000])



