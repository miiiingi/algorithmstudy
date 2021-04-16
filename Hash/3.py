import collections
def solution(clothes) : 
    clothlist = {}
    answer = 1
    for ind in range(len(clothes)) : 
        clothlist[clothes[ind][0]] = clothes[ind][1]
    clothcount = collections.Counter(clothlist.values())
    for count in clothcount.values() : 
        answer *= (count+1)
    return answer - 1
answer = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
print(answer)