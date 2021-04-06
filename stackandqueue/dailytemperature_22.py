# 문제
# 매일 화씨 온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
# un solved
import collections
def daily(T) : 
    answer = [] 
    for ind, item in enumerate(T) : 
        count = 0 
        if max(T[ind:]) == item : 
            answer.append(count)
            continue
        else : 
            for comp in T[ind+1:] : 
                if item < comp :  
                    count += 1
                    answer.append(count)
                    break
                elif item >= comp : 
                    count += 1
    return answer 

def daily2(T) : 
    index = collections.deque([x for x in range(len(T))])
    count = [] 
    while index :
        stack = [] 
        _pop = index.popleft()
        stack.append(_pop)
        for ind in range(_pop + 1, len(T)) : 
            if T[_pop] < T[ind] :  
                stack.append(ind)
                break
        if len(stack) == 2 :  
            count.append(stack[1] - stack[0])
        else : 
            count.append(0)
    return count

def daily3(T) : 
    count = [0 for _ in range(len(T))] 
    stack = [] 
    T = collections.deque(T) 
    for ind, item in enumerate(T) :
        while stack and T[stack[-1]] < item :  
            last = stack.pop()
            count[last] = ind - last
        stack.append(ind)
    return count
        
        

answer = daily([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
answer2 = daily2([73, 74, 75, 71, 69, 72, 76, 73])
answer3 = daily3([73, 74, 75, 71, 69, 72, 76, 73])

# [1, 1, 4, 2, 1, 1, 0, 0]
print(answer3)


                