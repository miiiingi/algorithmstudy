import collections
N, M, V = map(int, input().split())
graph = {} 
# for iter in range(N) : 
#     graph[(iter+1)] = [] 
for iter in range(M) : 
    v1, v2 = map(int, input().split())
    if v1 not in graph : 
        graph[v1] = [] 
        graph[v1].append(v2)
    if v2 not in graph : 
        graph[v2] = []
        graph[v2].append(v1)
print(graph)
def dfs(start, discovered = collections.deque([])) :
    discovered.append(start)
    for w in graph[start] : 
        if w not in discovered : 
            discovered = dfs(w, discovered)
    return discovered
result_dfs = dfs(start = V)
print(result_dfs)