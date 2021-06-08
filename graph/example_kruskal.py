mygraph = {
    'vertices' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges' : [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}
parent = dict()
rank = dict()

def find(node) : 
    if parent[node] != node : 
        parent[node] = find(parent[node])
    return parent[node]

def union(v, u) : 
    root_v = find(v)
    root_u = find(u)

    if rank[root_v] > rank[root_u] : 
        parent[root_u] = root_v
    else : 
        parent[root_v] = root_u
        if rank[root_v] == rank[root_u] : 
            rank[root_u] += 1

def make_set(node) : 
    parent[node] = node
    rank[node] = 0

def kruskal(graph) : 
    mst = list()

    for node in graph['vertices'] : 
        make_set(node)
    
    edges = graph['edges']
    edges.sort()
    print(edges)

    for edge in edges : 
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u) : 
            union(node_v, node_u)
            mst.append(edge)
    return mst
answer = kruskal(mygraph)
print(answer)
    
