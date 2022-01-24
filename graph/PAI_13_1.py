import collections
import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0]].append([time[2], time[1]])
        visited = []
        que = [(0, k)]
        accum = collections.defaultdict(int)
        while que:
            pops = heapq.heappop(que)
            if not pops[1] in visited:
                visited.append(pops[1])
                # 순수하게 단일 경로에 대한 비용만 계산 > 순환하는 구조에서 이용될 수 있음
                accum[pops[1]] = pops[0]
                # if set(visited) == set(graph.keys()):
                #     return pops[0]
                for g in graph[pops[1]]:
                    heapq.heappush(que, (g[0] + pops[0], g[1]))
        print(accum)
        if set(visited) == set(graph.keys()):
            return max(accum.values())
        return -1 

sol = Solution()
# answer = sol.networkDelayTime(times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2)
answer = sol.networkDelayTime(times=[[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n=4, k=1)
# answer = sol.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=2)
# answer = sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
print(answer)
