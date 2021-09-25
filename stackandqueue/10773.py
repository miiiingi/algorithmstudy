import sys
import collections
input = sys.stdin.readline
array = collections.deque()
N = int(input().strip())
for _ in range(N) : 
    number = input().strip()
    if number == '0' : 
        array.pop()
    else : 
        array.append(int(number))
print(sum(array))