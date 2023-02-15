import csv
import re

# 파일을 읽어오는 함수(리스트 형태로 변경해서 반환해줌)
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)

    output = []
    for i in reader:
        output.append(i)
        
    return output

# ,를 제거해서 반환하는 함수
def switchcsv(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))  # , 제거
            except:
                pass
    return listName