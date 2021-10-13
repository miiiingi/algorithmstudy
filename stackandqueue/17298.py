import sys
import collections
input = sys.stdin.readline
N = int(input())
array = collections.deque(map(int,input().split()))
stack = []
answer = [-1 for _ in range(N)]
# for n in range(N) :
#     number = array.popleft()
#     for x in array : 
#         if number < x : 
#             answer[n] = x
#             break
# print(*answer)
for ind, elem in enumerate(array) : 
    while stack and stack[-1] < elem : 
        answer[ind - 1] = elem
        break
    stack.append(elem)
print(*answer)


