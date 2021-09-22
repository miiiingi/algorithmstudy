import itertools
list_num = list()
n = int(input())
k = int(input())
for _ in range(n) : 
    number = input()
    list_num.append(number)
cat_num = itertools.combinations(list_num, k)
_answer = list() 
for nums in cat_num : 
    num = itertools.permutations(nums, k)
    for n in num : 
        str_sum = ''
        for s in n : 
            str_sum += s
        if str_sum not in _answer :
            _answer.append(str_sum)
print(len(_answer))


