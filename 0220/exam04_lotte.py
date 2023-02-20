from selenium import webdriver as wd  
from selenium.webdriver.common.by import By  
import matplotlib as mpl
import matplotlib.pyplot as plt

path = 'D:\\chromedriver_win32\\chromedriver.exe'
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get('https://www.lottecinema.co.kr/NLCHS/Movie/List?flag=1') # 드라이버를 통해 url에 접근

# 롯데시네마 영화 제목 / 예매율 / 조회수 크롤링
movie_ul = driver.find_element(By.CLASS_NAME, 'movie_list')
movie_li = movie_ul.find_elements(By.CLASS_NAME, 'screen_add_box')

movie_list = []
lst = []
for i in movie_li:
    title = i.find_elements(By.CLASS_NAME, 'tit_info')
    views = i.find_elements(By.CLASS_NAME, 'rate_info')
    stars = i.find_elements(By.CLASS_NAME, 'star_info')

    for t, v, s in zip(title, views, stars):
        v = v.text.split("예매율")[1]
        movie_list.append([t.text, v, s.text])
print(movie_list)


# 평점으로 나눔
movie_dic = {'9.5이상' : 0, '9.0이상' : 0, '8.0이상' : 0}
for item in movie_list:
     item = float(item[2])
     if item >= 9.5:
        movie_dic['9.5이상'] += 1
     elif item >= 9.0:
        movie_dic['9.0이상'] += 1
     elif item >= 8.0:
        movie_dic['8.0이상'] += 1

print(movie_dic)

font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(movie_dic.values(), labels=movie_dic.keys(), autopct='%.1f%%')
plt.show()






