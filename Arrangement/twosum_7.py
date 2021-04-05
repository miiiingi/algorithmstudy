# 문제
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 전략
# 리스트의 나머지부분과 정답과의 차이를 비교해가면서 진행
def sums(nums, target) : 
    answer = True 
    start = 0 
    while(answer) : 
        for ind, x in enumerate(nums[start: ]) :
            if ind == 0 :
                base = x
            else : 
                if (base + x) == target :
                    return [start, start + ind]
        start += 1
        if start == len(nums) : 
            break
def sums2(nums, target) : 
    for ind, num in enumerate(nums) : 
        diff = target - num
        indexlist = [x for x in range(len(nums)) if x != ind]
        for num2 in indexlist : 
            if diff == nums[num2] :
                return [ind, num2]

def sums3(nums, target) : 
    numlist = {}
    for ind, num in enumerate(nums) : 
        numlist[num] = ind
    
    for ind, num in enumerate(nums) : 
        if (target - num) in numlist and ind != numlist[(target -num)]: 
            return [ind , numlist[(target - num)]]

nums = [2, 7, 11, 15]
target = 9
answer =sums(nums, target)
answer2 = sums2(nums, target)
answer3 = sums3(nums, target)

print(answer)
print(answer2)
print(answer3)
