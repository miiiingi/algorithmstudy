import collections
N, M = map(int, input().split())
graph = [] 
graph_location = collections.defaultdict(list)
check = [] 
for row in range(N) : 
    graph.append(list(input()))
    check.append(list([1 for _ in range(M)]))
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
            if i < 0 or j+1< 0 or i >= N or j+1 >= M :
                pass
            else : 
                if graph[i][j+1] == '1' : 
                    graph_location[(i, j)].append((i, j+1))
            if i < 0 or j-1 < 0 or i >= N or j-1 >= M :
                pass
            else : 
                if graph[i][j-1] == '1' : 
                    graph_location[(i, j)].append((i, j-1))
    
def bfs(graph, i, j) : 
    if i == (N-1) and j == (M-1) : 
        return 
    discovered = [(i, j)]
    queue = collections.deque([(i, j)])
    while queue : 
        Q = [queue.popleft()]
        if graph[Q[0][0]][Q[0][1]] == '1' : 
            for loc in graph_location[Q[0]] : 
                if loc not in discovered : 
                    discovered.append((loc[0], loc[1]))
                    queue.append((loc[0], loc[1]))
                    check[loc[0]][loc[1]] += check[Q[0][0]][Q[0][1]]
            
bfs(graph, 0, 0)
print(check[N-1][M-1])
