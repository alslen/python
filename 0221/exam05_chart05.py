import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 데이터 테이블을 pandas의 DataFrame 자료형으로 저장한 뒤 csv파일에 저장하시오.

# sales = {
#     '1분기' : [500,690,1100,1500,1990,1020],
#     '2분기' : [450,700,1030,1650,2020,1600],
#     '3분기' : [520,820,1200,1700,2300,2200],
#     '4분기' : [610,900,1380,1850,2420,2550]
# }

# df = pd.DataFrame(sales, index=('2015','2016','2017','2018','2019','2020'))
# print(df)
# df.to_csv('sales.csv', encoding='utf-8-sig')

df = pd.DataFrame([[500,450,520,610],[690,700,820,900],[1100,1030,1200,1380],[1500,1650,1700,1850],[1990,2020,2300,2420],[1020,1600,2200,2550]],
index=[2015,2016,2017,2018,2019,2020], columns=['1분기', '2분기', '3분기', '4분기'])
print(df)

# 한글 처리
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 데이터프레임 자체를 이용해서 그래프 표현 가능
# DataFrame 그래프로 표현
df = df.transpose()  # 행 열 전환
df.plot()
plt.show()

df.to_csv('sales.csv', header=False)

######################

# 각각의 값을 따로 선언해서 DataFrame에 넣을 수 있음
y1 = [500,450,520,610]
y2 = [690,700,820,900]
y3 = [1100,1030,1200,1380]
y4 = [1500,1650,1700,1850]
y5 = [1990,2020,2300,2420]
y6 = [1020,1600,2200,2550]
df = pd.DataFrame([y1,y2,y3,y4,y5,y6], index=[2015,2016,2017,2018,2019,2020], columns=['1분기', '2분기', '3분기', '4분기'])

df.to_csv('sales1.csv', header=True)

#############################

# x = range(len(y1))
# xLabel = ['first', 'second', 'thrid', 'forth']
# plt.plot(x, y1, color='b')
# plt.plot(x, y2, color='orange')
# plt.plot(x, y3, color='green')
# plt.plot(x, y4, color='red')
# plt.plot(x, y5, color='purple')
# plt.plot(x, y6, color='brown')
# plt.title('2015~2020 Quarterly sales')
# plt.xlabel('Quarters')
# plt.ylabel('sales')
# plt.xticks(x, xLabel, fontsize=10)  # x축에 대한 설정
# plt.legend(['2015','2016','2017','2018','2019','2020'], loc = 'upper left')
# plt.show()

