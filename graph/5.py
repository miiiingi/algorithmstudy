import collections
import heapq
def solution(n, edge):
    answer = 0 
    graph = collections.defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited = collections.defaultdict(int)
    Q = [(1, 0)]
    while Q:
        node, cost = heapq.heappop(Q)
        if node not in visited:
            visited[node] = cost
            for node2 in graph[node]:
                heapq.heappush(Q, (node2, cost + 1))
    for value in visited.values() : 
        if max(visited.values()) == value : 
            answer += 1
    return answer 


answer = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(answer)
