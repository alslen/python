# p251
# 오류 발생 코드
import re

with open('singer2.csv', 'r') as inFp:
    header = inFp.readline() # readline() : 한 줄씩 읽어옴
    header = header.strip()  # strip() : 공백 제거
    print(header)

    header_list = header.split(',') # split(',') : 쉼표로 구분 -> 리스트에 저장
    print(header_list)
    print(header_list[1], header_list[6])

    for inStr in inFp:
        inStr = re.sub('"','',inStr)  # 숫자에 따옴표가 들어가지기 때문에 
        # print(inStr)  
        inStr = inStr.strip()
        # print(inStr)
        row_list = inStr.split(',')
        print(row_list)
        # youtube = int(row_list[6])
        # youtube = int(youtube/10000)
        # print(row_list[0], str(youtube)+"만")