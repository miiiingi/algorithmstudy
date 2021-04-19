N = int(input())
M = int(input())
graph = {}
for iter in range(M) : 
    v1, v2 = map(int, input().split())
    if v1 not in graph :
        graph[v1] = []
        graph[v1].append(v2)
    else :
        graph[v1].append(v2)
    if v2 not in graph :
        graph[v2] = []
        graph[v2].append(v1)
    else : 
        graph[v2].append(v1)
def dfs(v, discovered = []) : 
    discovered.append(v)
    for w in graph[v] : 
        if w not in discovered : 
            discovered = dfs(w, discovered)
    return discovered
answer = dfs(1)
print(len(answer) -1)
