def reverse(strings) : 
    answer = [] 
    for x in strings[::-1] : 
        answer.append(x)
    return answer
answer = reverse(['h','e','l','l','o'])
print(answer)
