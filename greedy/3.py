def solution(number, k):
    answer = [number[0]]
    for num in number[1: ]:
        while answer and answer[-1] < num and k > 0 :
            answer.pop()
            k -= 1
        answer.append(num)
    if k != 0 :
        answer.pop()
    return ''.join(answer)

answer = solution("77777", 1)
print(answer)
# def solution(number, k) : 
#     answer = ''
#     for ind in range(len(number)) : 
#         if k == 0 :
#             answer += number[ind:]
#             return answer 
#         if len(answer) == len(number) - k : 
#             return answer
#         comp = number[ind : ind + k +1]
#         if int(number[ind]) == int(max(comp)) : 
#             answer += number[ind]
#         else : 
#             k -= 1
#     if len(answer) == len(number) : 
#         return answer[:len(number) - k]
