import collections


def solution(tickets):
    graph = collections.defaultdict(collections.deque)
    for start, end in tickets:
        graph[start].append(end)

    def dfs(v, visited, discarded):
        if len(visited) == len(tickets) + 1:
            return
        visited.append(v)
        for ind in range(len(graph[v])):
            node = graph[v].popleft()
            discarded.append(node)
            dfs(node, visited, discarded)
        else : 
            graph[node].append(discarded.pop())
            # if len(visited) != len(tickets) + 1:
            #     visited.pop()
            #     graph[v].append(node)

    for k in graph.keys():
        graph[k] = collections.deque(sorted(graph[k]))
    visited = []
    discarded = collections.deque([])
    dfs("ICN", visited, discarded)
    return visited


# answer = solution([["ICN", "A"], ["A", "C"], ["C", "A"], ["A", "B"], ["B", "D"]])
answer = solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]])
