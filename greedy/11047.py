import sys
input = sys.stdin.readline
N, K = map(int, input().split())
array = list()
for _ in range(N) : 
    array.append(int(input()))
answer = 0 
while array : 
    pops = array.pop()
    if K // pops != 0 : 
        answer += K // pops
        K -= pops * (K // pops)
print(answer)
