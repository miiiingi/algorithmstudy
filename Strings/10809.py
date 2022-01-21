S = input()
order = [-1 for _ in range(26)]
answer = ''
for ind, s in enumerate(S) : 
    if order[ord(s) - 97] == -1 :  
        order[ord(s) - 97] = ind 
    else : 
        pass
for o in order :
    answer += f'{o} '
answer = answer.strip()
print(answer)
