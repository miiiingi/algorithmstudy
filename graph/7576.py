# 1. 입력이 주어졌을 때, 기점과 가지 못하는 점을 찾아야 함
# 2. 기점부터 4방향으로 하나씩 증가하는데, 막힌 경우는 가지 못 한다는 조건을 걸어서 진행
# 3. -1에 둘러쌓인 경우, 모두 완성할 수 없다. >> 연결된 것이 모두 -1인 경우 ??
# 4. 어떻게 완성 되었다는 것을 판단할 것 인가 ?? >> 하나씩 돌면서 판단 ? 매 반복마다 그렇게 ??
import collections
N, M = map(int,input().split())
graph = [] 
graph_location = collections.defaultdict(list)
# graph_judge = 
init = [] 
prohibit = [] 
for iter in range(M) : 
    graph.append(list(input().split()))
# Step 1.
for i in range(M) : 
    for j in range(N) : 
        if i-1 >= 0 :
            graph_location[(i, j)].append((i-1, j))
        elif i+1 < M :
            graph_location[(i+1, j)].append((i+1, j))
        elif j-1 >= 0 :
            graph_location[(i, j)].append((i, j-1))
        elif j+1 < N :
            graph_location[(i+1, j)].append((i, j+1))
print(graph_location)
exit()
def bfs(graph, i, j) :
    if i < 0 or j < 0 or i >= N or j >= M or graph[j][i] == '-1' :  # 요기서 시간
        return
    discovered = [(j, i)]
    queue = [(j, i)]
    while queue : 
        Q = queue.pop()
        if Q[1] > 0 and (Q[0]+1) >0 and Q[1] < N and (Q[0]+1) < M and graph[Q[0]+1][Q[1]] == '0' : 
            graph[Q[0]+1][Q[1]] = '1'  
            discovered.append((Q[0]+1,Q[1]))
        if graph[Q[0]-1][Q[1]] == '0' : 
            graph[Q[0]-1][Q[1]] = '1'  
            discovered.append((Q[0]-1,Q[1]))
        if graph[Q[0]][Q[1]+1] == '0' : 
            graph[Q[0]][Q[1]+1] = '1'  
            discovered.append((Q[0],Q[1]+1))
        if graph[Q[0]][Q[1]-1] == '0' : 
            graph[Q[0]][Q[1]-1] = '1'  
            discovered.append((Q[0],Q[1]-1))


    graph[j][i] = '1'
    return
        # Step 4.
start = init.pop()
bfs(graph, start[1], start[0])