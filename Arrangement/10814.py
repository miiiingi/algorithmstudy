import sys
input = sys.stdin.readline
answer_list = [] 
N = int(input())
for n in range(N) : 
    answer_list.append((input().split(), n))
answer_list = sorted(answer_list , key = lambda x : (int(x[0][0]), int(x[1])), reverse=False)
for answer in answer_list : 
    print(f'{answer[0][0]} {answer[0][1]}')