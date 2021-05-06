# numbers의 갯수 만큼 자릿수를 만들어가자.
# 만들어진 각각의 수들을 반복하면서 소수인지 아닌지 판단
# 소수를 어떻게 판단하지 ? 
from itertools import combinations
def solution(numbers) :
    ind = [x for x in range(len(numbers))]
    string = list(numbers) 
    for x in combinations(ind, 2) :
        print(x)
answer = solution('17')
print(answer)