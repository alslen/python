# apt_201910.csv 파일을 usecsv에 있는 함수를 사용하여 3개 출력
import usecsv
import re
import csv

ap = usecsv.opencsv('apt_201910.csv')
apt = usecsv.switchcsv(ap)

print(apt[:3])
# apt_201910.csv 총 개수
print(len(apt))

# 시군구 단지명 가격 ==> 6개 출력
for i in apt[:6]:
    print([i[0],i[4],i[-4]])

print()
# 강원도에 120 m2 이상 3억 이하 검색하기
# (시군구 단지명 가격 출력)
new_list = [["시군구", '단지명', '가격']]
for i in apt:
    try:
        if i[5]>=120 and i[-4]<= 30000 and re.match('강원', i[0]):
            new_list.append([i[0], i[4], i[-4]])
    except:
        pass

print(new_list[:4])

# 파일로 출력
# apt11.csv를 write모드로 생성시킴(없으면 생성됨)
# 파일에 값이 들어 갈때 데이터마다 개행되기 때문에 newline을 공백으로 둠(newline사용x)
# with open('apt11.csv', 'w',newline='') as f:
#     a = csv.writer(f, delimiter=',') # ,로 구분짓기 위해 delimiter를 사용
#     a.writerows(new_list) # new_list에 들어있는 값을 한 행씩(리스트씩) 파일에 값이 쓰여짐

##############
# 첫번째 행에 컴퓨터, 노트북, 태블릿
# 두번째 행에 100,80,60
# 리스트 형태로 표현
test_list = [['컴퓨터','노트북','태블릿'],[100,80,60]]
print(test_list)

# test.csv 파일로 내보내기
with open('test.csv','w',newline='') as f:
    a = csv.writer(f)
    a.writerows(test_list)

