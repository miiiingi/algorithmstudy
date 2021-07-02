def solution(number, k):
    answer = []
    for ind in range(len(number)-1):
        if number[ind] >= number[ind+1] : 
            answer.append(number[ind])
        else : 
            while answer and answer[-1] < number[ind+1] : 
                answer.pop()
                k -= 1
            if k == 0 : 
                answer.append(number[ind+1])
            else : 
                k -= 1



answer = solution("817", 1)
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
