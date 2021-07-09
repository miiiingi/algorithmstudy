import collections
import sys
iter = int(input())
for i in range(iter):
    answer = 0 
    number_student = int(sys.stdin.readline())
    couple = []
    for x in map(int, sys.stdin.readline().split()):
        couple.append(x)
    graph = collections.defaultdict(int)
    for m, c in zip(range(number_student), couple):
        graph[m + 1] = c
        numlist = [0 for _ in range(number_student)]

    def dfs(node, visited):
        if node in visited : 
            visited.append(node)
            return visited
        visited.append(node)
        visited = dfs(graph[node], visited)
        return visited

    for k in graph.keys():
        visited = []
        visited = dfs(k, visited)
        if visited[-1] == k : 
            for v in visited : 
                numlist[v-1] = 1
    for n in numlist : 
        if n == 0 : 
            answer += 1
    print(answer)
