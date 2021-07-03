import heapq
def make_graph(n, costs) : 
    graph = {}
    for i in range(n) : 
        graph[i] = [] 
    for cost in costs : 
        graph[cost[0]].append((cost[2], cost[1]))
        graph[cost[1]].append((cost[2], cost[0]))
    return graph
def solution(n, costs) : 
    graph = make_graph(n, costs) 
    Q = [(0, 0)]
    visited = {} 
    while Q :
        cost_s, start = heapq.heappop(Q)
        if start not in visited : 
            visited[start] = cost_s
            for cost_d, desti in graph[start] :  
                heapq.heappush(Q, (cost_d, desti))
    return sum(visited.values())
answer = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(answer)