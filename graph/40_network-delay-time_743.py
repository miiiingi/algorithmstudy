# 가중치가 없는 경우에는 BFS로 탐색할 수 있지만, 가중치가 있는 경우는 다르게 생각해서 다익스트라 알고리즘으로 접근해야함
# BFS로 최단거리를 따질 때는 단순히 길만 최단거리로 가는 경우를 생각하지만, 다익스트라 알고리즘에서는 가중치를 고려해야하기 때문에, 그것을 고려할 수 있는 힙 구조를 사용하게 된다.
import collections
import heapq
class Solution2 : 
    def networkDelayTime(self, times, N, K) : 
        graph = collections.defaultdict(list) 
        for u, v, w in times : 
            graph[u].append((v, w))
        Q = [(0, K)]
        dist = collections.defaultdict(int)
        while Q : 
            time, node = heapq.heappop(Q)
            if node not in dist : 
                dist[node] = time
                for v, w in graph[node] : 
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == N : 
            return max(dist.values())
        return -1

answer = Solution2().networkDelayTime([[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]], 8 , 3)
print(answer)
