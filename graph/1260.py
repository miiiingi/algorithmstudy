import collections
import heapq
N, M, V = map(int, input().split())
graph = {} 
for iter in range(N) : 
    graph[(iter+1)] = [] 
for iter in range(M) : 
    v1, v2 = map(int, input().split())
    heapq.heappush(graph[v1], v2)
    heapq.heappush(graph[v2], v1)
def dfs(start, discovered = []) :
    discovered.append(start)
    for w in graph[start] : 
        if w not in discovered : 
            discovered = dfs(w, discovered)
    return discovered
def bfs(start) : 
    discovered = [start]
    queue = collections.deque([start])
    while queue : 
        v = queue.popleft() 
        for w in graph[v] : 
            if w not in discovered : 
                discovered.append(w)
                queue.append(w)
    return discovered

result_dfs = dfs(start = V)
result_bfs = bfs(start= V)
print(" ".join(str(i) for i in result_bfs))
print(" ".join(str(i) for i in result_dfs))