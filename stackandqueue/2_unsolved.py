# 문제
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 구하라.
# un solved

def solution(prices) : 
    answer = [] 
    for ind in range(len(prices)) :  # range를 이용해서 인덱스를 받아오도록 만들었고,
        count = 0 
        for price2 in prices[(ind+1): ] : # range
            if prices[ind] <= price2 : 
                count += 1 
            else : 
                count += 1
                break
        answer.append(count)
    return answer
answer = solution([1, 2, 3, 2, 3])
print(answer)