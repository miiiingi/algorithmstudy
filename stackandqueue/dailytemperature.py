# 문제
# 매일 화씨 온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
# 75 ~ 76 가는 과정과 76 ~ 73을 가는 과정을 어떻게 분리해서 알고리즘으로 나타낼 것이냐 ?
# un solved
import collections
def daily(T) : 
    answer = [] 
    for ind, item in enumerate(T) : 
        remain = len(T) - 1 - ind
        count = 0 
        for comp in T[ind+1:] : 
            if item < comp :  
                count += 1
                answer.append(count)
                break
            elif item > comp : 
                if remain <= 1 :
                    continue
                else :
                    count += 1
    return answer 

answer = daily([73, 74, 75, 71, 69, 72, 76, 73])
# [1, 1, 4, 2, 1, 1, 0, 0]
print(answer)


                