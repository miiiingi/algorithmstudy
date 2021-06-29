# 자신의 뒤에꺼 보다만 크게 수를 추리자.
# while 반복문 돌면서 다음 것보다 작은 것들 discard에 넣고
# discard의 길이가 k가 되면 반복문 종료
def solution(number, k) : 
    discard = [] 
    for ind in range(len(number)) : 
        if len(discard) == k : 
            break
        if number[ind] < number[ind+1] : 
            discard.append(ind)
    number = list(number)
    for ind in discard : 
        number[ind] = ''
    return ''.join(number) 
answer = solution('4177252841', 4)
print(answer)