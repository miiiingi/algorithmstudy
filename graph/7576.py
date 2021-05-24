# 1. 입력이 주어졌을 때, 기점과 가지 못하는 점을 찾아야 함
# 2. 기점부터 4방향으로 하나씩 증가하는데, 막힌 경우는 가지 못 한다는 조건을 걸어서 진행
# 3. -1에 둘러쌓인 경우, 모두 완성할 수 없다. >> 연결된 것이 모두 -1인 경우 ??
# 4. 어떻게 완성 되었다는 것을 판단할 것 인가 ?? >> 하나씩 돌면서 판단 ? 매 반복마다 그렇게 ??
N, M = map(int,input().split())
graph = [] 
# graph_judge = 
init = [] 
prohibit = [] 
for iter in range(M) : 
    graph.append(list(input().split()))
# Step 1.
for i in range(N) : 
    for j in range(M) : 
        if graph[j][i] == '1' :
            init.append((j, i))
        elif graph[j][i] == '-1' : 
            prohibit.append((j, i))
        else : 
            pass
def bfs(graph, i, j) :
    for height in range(M) : 
        for width in range(N) : 
            return
        # Step 4.