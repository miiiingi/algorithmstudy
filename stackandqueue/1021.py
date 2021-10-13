import sys
import collections
input = sys.stdin.readline
K, N = map(int, input().split())
query = collections.deque(list(map(int, input().split())))
array = collections.deque([x+1 for x in range(K)])
base = 1
answer = 0 
def cir_left(array) :
    array.appendleft(array.pop())
    return array
def cir_right(array) :
    array.append(array.popleft())
    return array
while query : 
    length = len(array)
    pops = query.popleft()
    dist = array.index(pops)
    dist_res = length - dist
    if pops == base :
        array.popleft()
        if array : 
            base = array[0]
        continue
    if dist <= dist_res : 
        answer += dist 
        for _ in range(dist) : 
            array = cir_right(array)
        array.popleft()
        base = array[0]
        continue
    elif dist > dist_res : 
        answer += dist_res
        for _ in range(dist_res) : 
            array = cir_left(array)
        array.popleft()
        base = array[0]
        continue
print(answer)

