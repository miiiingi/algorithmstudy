# 전략 : 그냥 문제에 나와 있는 조건 그대로 옮기기
# 어떻게 시간을 줄일 것 인가 ? 후보 : sorted, 하나씩 비교하는 알고리즘을 해시 느낌으로 ??

import collections
def solution(phone_book) : 
    phone_book = collections.deque(phone_book)
    while phone_book : 
        comp = phone_book.popleft() #123
        for obj in range(len(phone_book)) : #12
            if phone_book[obj][:len(comp)] == comp or comp[:len(phone_book[obj])] == phone_book[obj] : 
                return False 
    return True 
# answer = solution(['119','97674223','1195524421'])
answer = solution(['123','12'])

print(answer)