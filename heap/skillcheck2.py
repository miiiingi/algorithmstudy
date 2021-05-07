# 문제 : 어떻게 중간중간 있는 문자를 찾을 것인가 ? / 어떻게 가장 많이 등장한 만큼 자릿수를 채울것인가 ? 
import collections
print('ABCDE' - 'ACD')
def solution(orders, course) : 
    orders = collections.deque(sorted(orders, key = lambda x : len(x)))
    result = [] 
    while orders : 
        count = 1 
        order = orders.popleft()
        if len(order) in course : 
            for order_comp in orders : 
                if order in order_comp : 
                    count += 1
                if count >= 2 : 
                    result.append(order)
                    break
        else : 
            continue
    return result 
# answer = solution(['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'], [2,3,4])
answer = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,4])

print(answer)