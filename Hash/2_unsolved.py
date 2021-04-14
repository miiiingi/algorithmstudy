# 전략 : 그냥 문제에 나와 있는 조건 그대로 옮기기
# 어떻게 시간을 줄일 것 인가 ? 후보 : sorted, 하나씩 비교하는 알고리즘을 해시 느낌으로 ??

import collections
def solution(phone_book) : 
    # phone_book = sorted(phone_book, key = lambda x : len(x)) 
    phone_book = collections.deque(phone_book)
    while phone_book : 
        comp = phone_book.popleft()
        for obj in range(len(phone_book)) :
            if phone_book[obj][:len(comp)] == comp : 
                return False 
    return True 
def solution2(phone_book) : 
    phone_books = {}
    for ind , number in enumerate(phone_book) : 
        phone_books[ind] = number 
    print(list(phone_books.values()[:3]))
    exit()
    for i in range(len(phone_books)) :
        comp = phone_books.pop(i)
        if comp in list(phone_books.values())[:len(comp)] : 
            return False
    return True
answer = solution2(['119','97674223','1195524421'])
# answer = solution(['123','12'])

print(answer)