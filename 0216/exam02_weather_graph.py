import pandas as pd
import matplotlib as mpl  
import matplotlib.pyplot as plt  # matplotlib.pyplot : 그래프를 그려주는 라이브러리

df = pd.read_csv('weather_select.csv', index_col='지역', encoding='euc-kr')  # weather_select.csv에서 지역 컬럼을 index로 지정

# 그래프그리기
# 한글
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트종류, 제목, 차트크기, 범례, 폰트 크기 설정
city_df = df.loc[['서울','인천','부산']]
print(city_df)
ax = city_df.plot(kind='bar', title='날씨', figsize=(12,7), legend=True,fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'],  fontsize=12)
plt.show()
