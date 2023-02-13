nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]

def max_count(nums):
    counts = {}   # 딕셔너리 초기화 #{1:3 2:2 3:2}
    for i in nums: # 1 1 2 2 3 2  3
        if i in counts:  # dict에 이미 있는 값(counts에 값이 있으면)
            counts[i] += 1 # value값을 말함(counts[i])

        else:  # dict에 없는 값
            counts[i] = 1

    return counts # 리턴된 변수는 함수 밖에서 바로 사용가능
  
counts = max_count(nums)
print(counts) # {1:4, 2:4, 3:5}
# counts dict에서 최대값 출력
max_num = max(counts.values())
print("최대값 ", max_num)


# key : value
# 1 : 4번
# 2 : 4번
# 3 : 5번
# maxKey : [3]

f = list()
# f = [] # list형
for key,count in counts.items():
    print(key, ":", count, "번")
    if count == max_num:
        f.append(key)  # count 값이 max인 키 값을 추가(list에)

print('maxKey : ', f)

###################################
def sum(num):
    hap = 0
    for i in range(1, num+1): # range(시작점,종료시점(+1))
        hap += i
    return hap


print("sum : ", sum(10)) # 1부터 10까지의 합 출력