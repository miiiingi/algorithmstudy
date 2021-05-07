# 입력으로 하나씩 받아서 아이디랑 이름이랑 매치시키자.
import collections
def solution(record) : 
    result = collections.defaultdict(str) 

    for rec in record : 
        _, uid, name = rec.split(' ')
        result[uid] = name
    print(result)
    answer = [] 
    return answer
answer =solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(answer)