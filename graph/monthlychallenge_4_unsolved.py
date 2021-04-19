# 1. 그래프로 나타내기
# 2. 어떻게 탐색하면서 경우를 종료시킬 건지 생각해보기
def solution(w, edges) : 
    graph = {}
    for edge in edges : 
        if edge[0] not in graph : 
            graph[edge[0]] = []
        if edge[1] not in graph : 
            graph[edge[1]] = [] 
        graph[edge[0]] = edge[1]
        graph[edge[1]] = edge[0]
    print(graph)
a = [-5, 0, 2, 1, 2]
edges = [[0,1], [3, 4], [2, 3], [0, 3]]
answer = solution(a, edges)
print(answer)