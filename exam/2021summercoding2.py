# 한 턴 씩 세면서 하나씩 정리해보자
# 전략 : 일단 t를 기준으로 작은 값으로 정렬한 다음 같은 값이 있는지 조사
# 만약 같은 값이 있다면, 우선순위가 높은 순서대로 빼자
import collections
def solution(t, r):
    concat = []
    daegi = []
    result = []
    time_current = 0
    number = 0 
    for ind, c in enumerate(list(zip(t, r))):
        concat.append([c, ind])
    concat = collections.deque(sorted(concat, key = lambda x : x[0][0]))
    while concat:
        for c in concat:
            if c[0][0] == time_current:
                daegi.append(c)
                number += 1
            else:
                time_current += 1
                break
        if daegi:
            daegi = collections.deque(sorted(daegi, key=lambda x: (x[0][1], x[1])))
            result.append(daegi.popleft()[1])
            # number -= 1
            # 요기서 두개를 뺐는데, 하나는 잔여물로 concat에 남아있다 > 이것을 어떻게 처리할 것인가 ? 
            for i in range(number):
                concat.popleft()
                number -= 1
    return result


answer = solution([0, 1, 3, 0], [0, 1, 2, 3])
# answer = solution([7, 6, 8, 1], [0, 1, 2, 3])
print(answer)
