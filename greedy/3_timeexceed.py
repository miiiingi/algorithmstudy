# 자신의 뒤에꺼 보다만 크게 수를 추리자.
# while 반복문 돌면서 다음 것보다 작은 것들 discard에 넣고
# discard의 길이가 k가 되면 반복문 종료
def solution(number, k) : 
    answer = ''
    for ind in range(len(number)) : 
        if k == 0 :
            answer += number[ind:]
            return answer 
        if len(answer) == len(number) - k : 
            return answer
        comp = number[ind : ind + k +1]
        if int(number[ind]) == int(max(comp)) : 
            answer += number[ind]
        else : 
            k -= 1
    if len(answer) == len(number) : 
        return answer[:len(number) - k]
answer = solution('4177252841', 4)
print(answer)