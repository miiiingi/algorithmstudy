import heapq
import sys
input = sys.stdin.readline
lists = list() 
list_answer = list()
N = int(input())
for _ in range(N) : 
    n = int(input())
    if n == 0 :
        if not lists :  
            list_answer.append(0) 
        else : 
            pops = heapq.heappop(lists)
            list_answer.append(pops)
    else : 
        heapq.heappush(lists, n)
for answer in list_answer : 
    print(answer)