import numpy as np
import usecsv

def switchcsv(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(j) 
            except:
                pass
    return listName

# listName = usecsv.switchcsv(usecsv.opencsv('quest.csv'))
listName = switchcsv(usecsv.opencsv('quest.csv'))
quest = np.array(listName)
print(quest)

# 5보다 큰 값
print(quest>5)  # quest>5 => true/false로 반환

# 5보다 큰 값은 100로 수정
print(quest[quest>5]) # 5보다 큰 값을 출력
quest[quest>5] = 100  # 5보다 큰 값을 찾아서 그 위치에서 100으로 변경시켜줌
print(quest)


###############
a = np.array([[1,2,3],[4,5,6]])
print(a)
a[1,1] = 55
print(a)
