import collections
import heapq
V, E = map(int, input().split())
K = int(input())
time = [] 
for iter in range(E) : 
    u, v, w = map(int,input().split())
    time.append([u, v, w])
class Solution : 
    def networkDelayTime(self, time, k) : 
        graph = collections.defaultdict(list)
        # node로 가는 최소비용이 들어있는 리스트
        dist = collections.defaultdict(int)
        for u, v, w in time : 
            graph[u].append((v, w))
        Q =[(k, 0)]
        while Q : 
            node, time = heapq.heappop(Q)
            if node not in dist : 
                dist[node] = time
                for v, w in graph[node] : 
                    time_cum = time + w
                    heapq.heappush(Q, (v, time_cum))
            else : 
                continue
        return dist
answer = Solution().networkDelayTime(time, K)
for v in range(1, V+1) : 
    if v in answer : 
        print(answer[v])
    else : 
        print('INF')



