class Solution : 
    graph = {}
    count = [] 
    count_max = [] 
    condition = True 
    def networkDelayTime(self, time, n , k) : 
        for v in range(1, n+1) :
            self.graph[v] = [-1 for _ in range(n)]
        for ind in range(len(time)) : 
            self.graph[time[ind][0]][time[ind][1]-1] = time[ind][2]
        self.dfs(k)
        if not self.condition : 
            return max(self.count)
        else : 
            return -1
    def dfs(self, k) : 
        for ind, g in enumerate(self.graph[k]) : 
            if g > 0 : 
                self.condition = False 
                self.count_max.append(self.graph[k][ind])
                self.graph[k][ind] = 0
                self.dfs(ind+1)
                self.count.append(sum(self.count_max))
                self.count_max = [] 
            elif g < 0 : 
                continue
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

# answer = Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1], [1, 5, 3]], 5 ,2)
answer = Solution2().networkDelayTime([[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]], 8 , 3)
print(answer)
