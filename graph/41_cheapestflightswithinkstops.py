import collections
import heapq
class Solution : 
    def findCheapestPrice(self, n, flights, src, dst, k) : 
        graph = collections.defaultdict(list)
        for u, v, w in flights : 
            graph[u].append((v, w))
        Q = [(0, src, 0)]
        while Q : 
            time, node, inter = heapq.heappop(Q)
            if node == dst : 
                return time
            if inter <= k : 
                inter += 1
                for v, w in graph[node] : 
                    heapq.heappush(Q, (time + w, v, inter))

answer = Solution().findCheapestPrice(3, [[0, 1, 100],[1,2,100],[0,2,500]], 0, 2, 0)
print(answer)