import collections
def solution(tickets) : 
    graph = collections.defaultdict(list)
    for start, end in tickets : 
        graph[start].append(end)
        for k in graph.keys() : 
            graph[k] = sorted(graph[k])
    # graph['ICN'] = sorted(graph['ICN'], key = lambda x : 1 if 'ICN' in graph[x] else 0, reverse=True)
    def dfs(v, visited = []) : 
        visited.append(v)
        for node in graph[v] : 
            graph[v].remove(node)
            graph[v].append(node)
            visited = dfs(node, visited)
    # 돌아돌아서 자신이 나오는 순서대로 정렬
        return visited
    while True : 
        visited = dfs('ICN') 
        if len(visited) == len(tickets) + 1 : 
            return visited

# answer = solution([['ICN','SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'], ['SFO', 'QRE']])
# 돌아오는 ICN이 우선순위가 되어야 갇혀 있지 않을 수 있음
# answer = solution([['ICN','B'], ['B', 'ICN'], ['ICN', 'A'], ['A', 'D'], ['D', 'A']])
# 돌아오는 ICN 보다 알파벳 순서가 먼저 있는 경우 (ICN을 먼저가지 않아도, 갇혀있지 않는 경우)
# answer = solution([['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO'], ['ICN','BOO'], ['ICN', 'COO'] ])
# 조금 더 일반적인 원리를 생각해보자.
# answer = solution([['ICN','JFK'], ['HND', 'IAD'], ['JFK', 'HND']])
answer = solution([['ICN','A'],['A','C'],['A','D'],['D','B'],['B','A']])
print(answer)