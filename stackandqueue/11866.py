import sys
import collections
input = sys.stdin.readline
N, K = map(int, input().split())
array = collections.deque([x + 1 for x in range(N)])
answer = '' 
while array :
    for _ in range(K-1) : 
        pops = array.popleft()
        array.append(pops)
    pops = array.popleft()
    answer += f'{pops}, '
answer = answer.strip()
answer = answer[:-1]
print(f'<{str(answer)}>')
    
