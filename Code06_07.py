import csv # csv : 데이터에 콤마가 들어간 경우에 유용하다

with open("singer2.csv", "r") as inFp:
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)  # 헤더 리스트가 바로 반환됨
    print(header_list[1], header_list[6])
    for row_list in csvReader:
        youtube = int(row_list[6].replace(',',''))
        youtube = int(youtube/10000)
        print(row_list[1], str(youtube)+"만")