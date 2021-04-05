# 문제
# 매일 화씨 온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
# un solved
import collections
def daily(T) : 
    answer = [] 
    for ind, item in enumerate(T) : 
        count = 1
        for comp in T[ind+1:] : 
            if item < comp :  
                answer.append(count)
                break 
            elif item > comp : 
                count += 1

    pass
answer = daily([73, 74, 75, 71, 69, 72, 76, 73])


                