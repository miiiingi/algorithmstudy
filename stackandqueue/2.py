# 문제
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 구하라.
# un solved

def solution(prices) : 
    answer = [0 for _ in range(len(prices))] 
    for ind in range(0, len(prices)) : 
        count = 0 
        for ind2 in range(ind+1, len(prices)): 
            count += 1 
            if prices[ind] > prices[ind2] : 
                break
        answer[ind] = count
    return answer
answer = solution([1, 2, 3, 2, 3])
print(answer)