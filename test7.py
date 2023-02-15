import re
import csv

f = open('popSeoul.csv', 'r')  
reader = csv.reader(f)  # reader() : open한 csv파일을 읽을 수 있음

output = []
print(reader)  # 객체값이 출력됨
for i in reader:
    tmp = [] 
   # print(i)  # 한줄의 리스트 형식으로 반환 -> 하나하나씩 읽어오기 위해 이중 for문을 돌림
    for j in i:
        try:  # 문자열 인것도 있기 때문에 예외처리를 해줘야함(문자열에 콤마를 제거할 수 없기 때문에)
            if re.search('\d', j):  # 숫자인것만 뽑아냄
                tmp.append(float(re.sub(',', '', j))) # , 제거하고 출력  # float형으로 형 변환
            else:  # 문자열인 경우
                tmp.append(j)
        except:
            pass

    output.append(tmp)

print(output)

# a = 100.56
# print(round(a, 1)) # 반올림

# 외국인 비율이 5% 넘는 구만 출력(구, 한국인, 외국인, 외국인 비율(%) ==> 외국인/(한국인+외국인))
result = [['구', '한국인', '외국인','외국인비율(%)']]
for i in output:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 5:
            i[3] = foreign
            # result.append(i[0], i[1], i[2], foreign)  foreign을 리스트 안에 들어가게 만들어줘야함. -> 그래서, 리스트 안에 리스트가 들어가져야함
            result.append([i[0], i[1], i[2], foreign])  
            # print(i[0], i[1], i[2], foreign)
    except:
        pass # 안 되는 것은 무시

### 출력
print(result)
  





