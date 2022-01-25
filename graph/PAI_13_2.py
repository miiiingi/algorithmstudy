from typing import List
import collections
import heapq
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for time in flights:
            graph[time[0]].append([time[2], time[1]])
        que = [[0, src, 0]]
        accum = collections.defaultdict(int)
        while que:
            pops = heapq.heappop(que)
            if not pops[1] in accum:
                if pops[2] > k + 1:
                    del accum[rsv[1]]
                    continue
                # 순수하게 단일 경로에 대한 비용만 계산 > 순환하는 구조에서 이용될 수 있음
                accum[pops[1]] = pops[0]
                if pops[1] == dst:
                    return accum[dst]
                for g in graph[pops[1]]:
                    heapq.heappush(que, [g[0] + pops[0], g[1], pops[2] + 1])
                rsv = pops[:]
        if len(accum.keys()) == n:
            return max(accum.values())
        return -1


sol = Solution()
# answer = sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
# answer = sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
# answer = sol.findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1)
answer = sol.findCheapestPrice(4, [[0, 1, 1], [1, 2, 1], [0, 2, 5], [2, 3, 1]], 0, 3, 1)
print(answer)

