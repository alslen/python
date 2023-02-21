import matplotlib.pyplot as plt
import wordcloud

keywords = {'안녕':2, '하세요':1, '빅데이터':15, '웹크롤링':3}

wc = wordcloud.WordCloud(font_path='c:/Windows/fonts/malgun.ttf')  # 한글을 사용할 것이면 반드시, 한글폰트를 지정해줘야함.
cloud = wc.generate_from_frequencies(keywords)  # 미리 정의된 단어의 빈도수 를 이용하여 워드 클라우드를 그림

figure = plt.figure()
plt.imshow(cloud)  # 템플릿을 이용하여 워드클라우드를 생성
plt.show()
figure.savefig('word.png') # 생성한 워드클라우드를 그림으로 저장