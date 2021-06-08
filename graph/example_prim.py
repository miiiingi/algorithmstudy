myedges = [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (8, 'B', 'C'),
    (9, 'B', 'D'), 
    (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (11, 'F' ,'G')
]
from collections import defaultdict
from heapq import * 
def prim(node_start, edges) : 
    mst = []
    adjacent_edges = defaultdict(list)
    for weight, u, v in edges : 
        adjacent_edges[u].append((weight, u, v))
        adjacent_edges[v].append((weight, v, u))
    node_visited = set(node_start)
    candidate_edge_list = adjacent_edges[node_start]
    heapify(candidate_edge_list)

    while candidate_edge_list : 
        weight, u, v = heappop(candidate_edge_list)
        if v not in node_visited :
        # 이미 방문했다는 것은 같은 부모를 가지고 있다는 뜻이니까, 방문하지 않은 것들 중에서 가장 최소의 값을 가지는 것을 탐색하면서 진행 > 자연스레 cyclic한 것이 제외
            node_visited.add(v)
            mst.append((weight, u, v))

            for edge in adjacent_edges[v] : 
                if edge[2] not in node_visited : 
                    heappush(candidate_edge_list, edge)
    return mst 
answer = prim('A', myedges)
print(answer)