# 자신의 뒤에꺼 보다만 크게 수를 추리자.
# while 반복문 돌면서 다음 것보다 작은 것들 discard에 넣고
# discard의 길이가 k가 되면 반복문 종료
import collections
def solution(number, k) : 
    discard = [] 
    candidate = collections.deque([])
    for ind in range(len(number)) : 
        if len(discard) == k : 
            break
        if ind in discard : 
            continue
        if candidate : 
            candi = candidate.popleft()
            if number[candi] < number[ind] :  # 같은 경우도 처리해야함
                discard.append(candi)
        if number[ind] < number[ind+1] : 
            discard.append(ind)
        elif number[ind] > number[ind+1] : 
            candidate.append(ind)
            discard.append(ind+1)
        else : 
            pass

    number = list(number)
    for ind_discard in discard : 
        number[ind_discard] = ''
    return ''.join(number) 
answer = solution('4177252841', 4)
print(answer)