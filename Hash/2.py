# 전략 : 그냥 문제에 나와 있는 조건 그대로 옮기기
# 어떻게 시간을 줄일 것 인가 ? 후보 : sorted, 하나씩 비교하는 알고리즘을 해시 느낌으로 ??
# 왜 시간초과가 뜰까 ? >> 하나씩 비교하기 때문에, 끝에 두 개가 있으면 너무 많은 시간이 걸림 >> 어떻게 선택지를 줄일 것인가 또는 어떻게 탐색하는 시간을 줄일 것인가 ?? 
# 어떻게 선택지를 줄일 것인가는 두개씩만 비교해서 없으면 break >> sort를 잘하면 딱 순서대로 되기 때문에 가능! >> 항상 이런 문제면 sort를 잘 생각해보기!!
import collections
def solution(phone_book) : 
    phone_book.sort()
    phone_book = collections.deque(phone_book)
    while phone_book : 
        comp = phone_book.popleft() #123
        for obj in range(len(phone_book)) : #12
            if phone_book[obj][:len(comp)] == comp : 
                return False
            else : 
                break
    return True 