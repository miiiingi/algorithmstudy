import sys
import collections
input = sys.stdin.readline
N = int(input())
array = collections.deque([x+1 for x in range(N)])
while len(array) != 1 : 
    pops = array.popleft()
    pops2 = array.popleft()
    array.append(pops2)
print(array[0])

