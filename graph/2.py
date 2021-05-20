import collections
def solution(n, computers) : 
    result = 0 
    graph = collections.defaultdict(list)
    check_array = [] 
    for i in range(len(computers)) : 
        for j in range(len(computers)) : 
            if computers[i][j] == 1 : 
                graph[i].append(j)

    def dfs(graph, node) : 
        if not node in check_array : 
            check_array.append(node)
            for arrive in graph[node] : 
                dfs(graph, arrive)
    for ind in range(len(computers)) : 
        if ind in check_array : 
            continue
        else : 
            dfs(graph, ind)
            result += 1
    return result
answer = solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(answer)