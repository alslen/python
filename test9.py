import usecsv  # 내가 작성한 파일을 사용하기 위해서도 import를 해줘야함

total = usecsv.opencsv('popSeoul.csv')
resultList = usecsv.switchcsv(total)

print(resultList[:4])

newList = [['구', '한국인', '외국인', '외국인비율(%)']]

for i in resultList:
    f = 0
    try:
        f = round(i[2]/(i[1]+i[2])*100, 1)
        if f>7:
            newList.append([i[0],i[1],i[2],f])
    except:
        pass

print(newList)
