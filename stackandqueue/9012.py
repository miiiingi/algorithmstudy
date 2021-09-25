import sys
input = sys.stdin.readline
answer = list()
N = int(input())
for _ in range(N) : 
    array = input().strip()
    comp = list()
    for a in array : 
        if a == '(' : 
            comp.append(a)
        elif a == ')' : 
            if comp and comp[-1] == '(' : 
                comp.pop()
            else : 
                comp.append(a)
    if not comp : 
        answer.append('YES')
    else : 
        answer.append('NO')
for a in answer :
    print(a)


