import csv
import re

def opencsv(filename):
    f = open('popSeoul2.csv', 'r')
    reader = csv.reader(f)

    output = []
    for i in reader:
        output.append(i)
        
    return output

total = opencsv('popSeoul2.csv')
print(type(total))
print(total[:5])   # 5개만 출력(리스트 안에 각각의 리스트가 들어가는 것을 확인할 수 있음)
for i in total[:5]:
    print(i)  # 각각의 리스트만 출력해주기 위해 for를 사용

# 원본을 직접 수정하기 위해 위치값을 구해옴(index로)
print()
for i in total[:5]:
    for j in i:
        # print(i.index(j))  # i에서 j의 위치 확인(index를 이용)
        try:
            i[i.index(j)] = float(re.sub(',','',j))  # , 제거
        except:
            pass

print(total[:5])
print()
print(total)

test = [10,20,30,40,50]

# 50의 위치값
print(test.index(50))

# 쉼표를 제거하고 float와 int형으로 형 변환
j = '1,468,246'
print(float(re.sub(',','',j)))
print(int(re.sub(',','',j)))
