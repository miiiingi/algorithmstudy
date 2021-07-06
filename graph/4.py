import collections
def solution(tickets) : 
    graph = collections.defaultdict(list)
    for start, end in tickets : 
        graph[start].append(end)
    graph['ICN'] = sorted(graph['ICN'])
    visited = [] 
    Q = collections.deque([('ICN', 'ICN')])
    while Q : 
        start, end = Q.popleft()
        visited.append(end)
        for v in graph[end] :  
            Q.append((end, v))


    answer = []  
    return answer
answer = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(answer)