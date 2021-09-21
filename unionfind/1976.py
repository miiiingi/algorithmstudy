import sys
import collections
input = sys.stdin.readline
num_cities = int(input())
num_nodes = int(input())
graph = [] 
graph_cities = collections.defaultdict(list)
for n in range(num_cities) : 
    graph.append(list(input().split()))
for n1 in range(num_cities) : 
    for n2 in range(num_cities) : 
        node = graph[n1][n2]
        if node == '1' : 
            graph_cities[n1+1].append(n2+1)