# 1. 입력이 주어졌을 때, 기점과 가지 못하는 점을 찾아야 함
# 2. 기점부터 4방향으로 하나씩 증가하는데, 막힌 경우는 가지 못 한다는 조건을 걸어서 진행
# 3. -1에 둘러쌓인 경우, 모두 완성할 수 없다. >> 연결된 것이 모두 -1인 경우 ??
# 4. 어떻게 완성 되었다는 것을 판단할 것 인가 ?? >> 하나씩 돌면서 판단 ? 매 반복마다 그렇게 ??
import collections
N, M = map(int,input().split())
graph = [] 
init = [] 
check = [] 
for iter in range(M) : 
    graph.append(list(input().split()))
    check.append(list([1 for _ in range(N)]))
# Step 1.
for i in range(M) : 
    for j in range(N) : 
        if graph[i][j] == '1' :
            init.append((i, j))
def bfs(graph, start) :
    queue = collections.deque([])
    for loc_start in start : 
        queue.append(loc_start)
    while queue : 
        Q = queue.popleft()
        candi_coor = [(Q[0]-1, Q[1]), (Q[0]+1, Q[1]), (Q[0], Q[1]-1), (Q[0], Q[1]+1)]
        for loc in candi_coor :
            if loc[0] < 0 or loc[1] < 0 or loc[0] >= M or loc[1] >= N or graph[loc[0]][loc[1]] == '-1':
                continue
            if graph[loc[0]][loc[1]] == '0' : 
                graph[loc[0]][loc[1]] = '1'
                queue.append((loc[0], loc[1]))
                check[loc[0]][loc[1]] += check[Q[0]][Q[1]]

bfs(graph, init)
max_base = 0
possible = True 
for i in range(M) : 
    for j in range(N) : 
        if graph[i][j] == '0' : 
            possible = False
        if check[i][j] > max_base : 
            max_base = check[i][j]
if possible : 
    print(max_base-1)
else : 
    print(-1)