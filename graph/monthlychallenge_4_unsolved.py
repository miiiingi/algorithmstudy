# 1. 그래프로 나타내기
# 2. 어떻게 탐색하면서 경우를 종료시킬 건지 생각해보기, 순서는 상관없나 ? , 어떻게 순서를 배당할 것 인가?
import collections
def solution(a, edges) : 
    graph = collections.defaultdict(list)
    for start, end in edges : 
        graph[start].append(end)
    while True : 
        for v in graph : 
            for e in graph[v] : 
                if a[v] != 0 and a[e] == 0 :
                    continue
                elif a[v] != 0 and a[e] != 0 : 

        break
    return answer
answer = solution([-5, 0, 2, 1, 2], [[0,1],[3,4],[2,3],[0,3]])
print(answer)