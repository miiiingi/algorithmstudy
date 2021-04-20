# 1. 그래프로 나타내기
# 2. 어떻게 탐색하면서 경우를 종료시킬 건지 생각해보기, 순서는 상관없나 ? , 어떻게 순서를 배당할 것 인가?
def dfs(start, a, graph, discovered = [], count = 0) : 
    discovered.append(start)
    for w in graph[start] : 
        if a[w] == 0 :  
            continue
        else : 
            if w not in discovered : 
                while True : 
                    if a[w] < 0 : 
                        a[w] += 1
                        a[start] -= 1
                        count += 1
                        if a[w] == 0 : 
                            break
                    elif a[w] > 0 :
                        a[w] -= 1
                        a[start] += 1
                        count += 1
                        if a[w] == 0 : 
                            break
                discovered, count = dfs(w, a, graph, discovered, count)
    return discovered, count

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
    graph = dict(sorted(graph.items(), key = lambda x : len(x[1]), reverse=True))
    answer =  dfs(list(graph.keys())[0], a, graph) 
    if answer[1] == 0 :
        return -1
    else : 
        return answer[1]
a = [-5, 0, 2, 1, 2]
edges = [[0,1], [3, 4], [2, 3], [0, 3]]
answer = solution(a, edges)
print(answer)