def solution(number, k):
    answer = []
    for ind in range(len(number)):
        if k == 0:
            return "".join(answer) + number[ind:]
        if len(answer) == len(number) - k:
            return "".join(answer)
        if number[ind] >= number[ind + 1]:
            if not answer:
                answer.append(number[ind])
                continue
            if answer[-1] < number[ind]:
                answer.pop()
                k -= 1
            answer.append(number[ind])
        else:
            k -= 1


answer = solution("99919", 1)
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
