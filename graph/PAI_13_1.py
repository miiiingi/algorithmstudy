import collections
import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0]].append([time[2], time[1]])
        visited = []
        que = [(0, k)]
        while que:
            pops = heapq.heappop(que)
            if not pops[1] in visited:
                visited.append(pops[1])
                # if set(visited) == set(graph.keys()):
                #     return pops[0]
                for g in graph[pops[1]]:
                    g[0] += pops[0]
                    heapq.heappush(que, (g[0], g[1]))
        if set(visited) != set(graph.keys()):
            return -1
        else:
            return pops[0] 

sol = Solution()
# answer = sol.networkDelayTime(times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2)
answer = sol.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=2)
# answer = sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
print(answer)
