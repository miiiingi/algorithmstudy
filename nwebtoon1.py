import collections
def solution(S, pattern) : 
    answer = 0 
    for ind in range(len(S) - len(pattern)+1) : 
        if S[ind] not in pattern : 
            continue
        comp = S[ind : ind + len(pattern)]
        if collections.Counter(pattern) == collections.Counter(comp) :
            answer += 1
    return answer
answer = solution("tegsornamwaresomran", 'ransom')
print(answer)