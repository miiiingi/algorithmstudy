for i in range(5) : 
    for j in range(5) : 
        if 1<=j<=3 : 
            continue
        print((i,j))
exit()

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
def recursive_dfs(v, discovered = []) :
    discovered.append(v)
    for w in graph[v] : 
        if not w in discovered : 
            discovered = recursive_dfs(w, discovered)
    return discovered

def iterative_dfs(start_v) : 
    discovered = []
    # stack이 방문해야할 위치를 가르킨다고 생각하면 편할 듯!(역순으로 가자)
    stack = [start_v]
    while stack : 
        v = stack.pop()
        if v not in discovered :
            discovered.append(v)
            for w in graph[v] : 
                stack.append(w)
    return discovered
def iterative_bfs(start_v) : 
    discovered = [start_v]
    queue = [start_v]
    while queue : 
        v = queue.pop(0)
        for w in graph[v] :
            if w not in discovered : 
                discovered.append(w)
                queue.append(w)
    return discovered
result_recursive_dfs = recursive_dfs(1)
result_iterative_dfs = iterative_dfs(1)
result_iterative_bfs = iterative_bfs(1)
