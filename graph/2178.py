import collections
N, M = map(int, input().split())
graph = [] 
graph_location = collections.defaultdict(list)
check = [] 
result = 0
for row in range(N) : 
    graph.append(list(input()))
for i in range(N) : 
    for j in range(M) : 
        if graph[i][j] == '1' : 
            # if (i, j) not in graph_location : 
            if i+1 < 0 or j < 0 or i+1 >= N or j >= M :
                pass
            else : 
                if graph[i+1][j] == '1' : 
                    graph_location[(i, j)].append((i+1, j))
            if i-1 < 0 or j < 0 or i-1 >= N or j >= M :
                pass
            else : 
                if graph[i-1][j] == '1' : 
                    graph_location[(i, j)].append((i-1, j))
            if i < 0 or j+1< 0 or i+1 >= N or j+1 >= M :
                pass
            else : 
                if graph[i][j+1] == '1' : 
                    graph_location[(i, j)].append((i, j+1))
            if i < 0 or j-1 < 0 or i >= N or j-1 >= M :
                pass
            else : 
                if graph[i][j-1] == '1' : 
                    graph_location[(i, j)].append((i, j-1))
    
def dfs(graph, i, j) : 
    if i >= N or j >= M or graph[i][j] == '0' :
        return
    if i == (N-1) and j == (M-1) : 
        return
    graph[i][j] = '0'
    check[i][j] += 1
    # location.append((i, j))
    if i+1 >= N : 
        return 
    else : 
        check[i+1][j] = check[i][j]
        dfs(graph, i+1, j)
    if j+1 >= M :
        return
    else :
        check[i][j+1] = check[i][j]
        dfs(graph, i, j+1)

def bfs(graph, i, j) : 
    return
dfs(graph, 0, 0)
print(result)
