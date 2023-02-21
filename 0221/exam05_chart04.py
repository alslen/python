import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

# weather_select.csv 파일을 읽어서
# 서울, 인천, 대전, 대구, 광주, 부산, 울산 지역의 기온, 습도를 선그래프로 출력
df = pd.read_csv('weather_select.csv', index_col='지역', encoding='cp949')  #  index_col='지역' : 지역을 기준으로 해서 파일을 읽어옴
# print(df)
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
print(city_df)

xdata = ['서울', '인천', '대전', '대구', '광주', '부산', '울산'] # x축 데이터
temp = city_df['온도']
hum = city_df['습도']
print(temp)

# 폰트 지정(한글을 사용하기 위해 지정)
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 선 그래프
# plt.figure(figsize=(10,6))
# plt.plot(xdata, temp, label='기온')
# plt.plot(xdata, hum, label='습도')
# plt.legend()
# plt.show()

# 막대 그래프
# figure = plt.figure()
# axes = figure.add_subplot(111)
# axes.bar(xdata, hum)
# axes.bar(xdata, temp)  # temp를 먼저 쓰면 hum에 그래프가 가려짐.
# axes.legend(['습도','기온'])  # 먼저 온 것을 먼저 써 줘야함.
# plt.show()

# 데이터프레임이 가지는 속성(plot)을 통해서 그래프를 그릴 수 있음
ax = city_df.plot(kind='bar', title='날씨', figsize=(12,7), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온','습도'], fontsize=12)
plt.show()


