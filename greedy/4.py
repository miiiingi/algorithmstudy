# 일단 오름차순으로 정리해서 순서대로 더해보고 되는데까지 하나로 묶어서 popleft
import collections
def solution(people, limit) : 
    people = collections.deque(sorted(people))
    answer = 0
    while people : 
        person = people.pop()
        if not people : 
            return answer + 1
        if person + people[0] <= limit : 
            people.popleft()
        answer += 1
    return answer
answer = solution([70, 50, 80], 100)
print(answer)
