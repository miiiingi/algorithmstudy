# 1. 그래프로 나타내기
# 2. 어떻게 탐색하면서 경우를 종료시킬 건지 생각해보기, 순서는 상관없나 ? , 어떻게 순서를 배당할 것 인가?
def dfs(a, v, graph) : 
    count = 0 
    candidate = [] 
    for w in graph[v] : 
        candidate.append(w)
        if a[w] == 0 : 
            continue
        else : 
            condition_nonzero = True 
            while condition_nonzero : 
                if a[v] != 0 and a[w] == 0 and a[candidate[-1]] == 0 : 
                    pass
                if a[v] == 0 or a[w] == 0 :
                    break
                if a[v] < 0 :
                    a[v] += 1
                    a[w] -= 1
                    count += 1
                elif a[v] > 0 :
                    a[v] -= 1
                    a[w] += 1
                    count += 1
    return count

def solution(a, edges) : 
    graph = {}
    count_concat = 0 
    for edge in edges : 
        if edge[0] not in graph : 
            graph[edge[0]] = []
        if edge[1] not in graph : 
            graph[edge[1]] = [] 
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    for v in graph.keys() :
        if a[v] == 0 : 
            continue
        else : 
            count_concat += dfs(a, v, graph)
    return count_concat
a = [-5, 0, 2, 1, 2]
edges = [[0,1], [3, 4], [2, 3], [0, 3]]
answer = solution(a, edges)
print(answer)