# 몇번 거쳤는지에 대한 변수를 따로 만들어야 하는데, 그것을 어떻게 카운트하지 ? 
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
                    alt = time + w
                    heapq.heappush(Q, (alt, v, inter))
        return -1

# answer = Solution().findCheapestPrice(3, [[0, 1, 100],[1,2,100],[0,2,500]], 0, 2, 2)

class Solution2 : # 조금 더 깔끔하게 짜기!
    def findCheapestPrice(self, n, flights, src, dst, k) : 
        graph = collections.defaultdict(list) 
        for u, v, w in flights : 
            graph[u].append((v, w))
        Q = [(0, src, k)]
        while Q : 
            time, node, inter = heapq.heappop(Q)
            if node == dst : 
                return time
            if k >= 0 : 
                for v, w in graph[node] : 
                    alt = time + w
                    heapq.heappush(Q, (alt, v, inter-1))
        return -1
answer = Solution2().findCheapestPrice(3, [[0, 1, 100],[1,2,100],[0,2,500]], 0, 2, 2)
print(answer)


