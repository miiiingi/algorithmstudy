import sys
input = sys.stdin.readline
N = int(input())
array = sorted(list(map(int, input().split()))) # O(N)
answer= list()
base = abs(array[0] + array[1])
answer.append((array[0], array[0 + 1]))
for ind in range(1, N - 1) : 
    if abs(array[ind] + array[ind + 1]) <= base : 
        answer.pop()
        base = abs(array[ind] + array[ind + 1])
        answer.append((array[ind], array[ind + 1]))
print(*answer[0])




