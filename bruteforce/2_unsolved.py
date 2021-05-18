# numbers의 갯수 만큼 자릿수를 만들어가자. >> 어떻게 자릿수만큼의 수를 만들지 ? 
# 만들어진 각각의 수들을 반복하면서 소수인지 아닌지 판단
# 소수를 어떻게 판단하지 ? 
from itertools import combinations
def solution(numbers) :
    result = [] 

    def iterations(index, path, limit_length) : 
        if limit_length == 0  : 
            result.append(path[:])

        for ind_inter in range(index, len(numbers)) : 
            path.append(numbers[ind_inter])
            iterations(ind_inter + 1, path, limit_length - 1)
            path.pop()

    length = len(numbers)
    for number_limit in range(1, length + 1) : 
        for ind in range(length) : 
            iterations(ind, [], number_limit)
    # print(int('011'))
    # ind = [x for x in range(len(numbers))]
    # string = list(numbers) 
    # for x in combinations(ind, 2) :
    #     print(x)
answer = solution('17')
print(answer)