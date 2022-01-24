import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0]].append([time[2], time[1]])
        visited = [k]
        que = list()
        que.append([0, k])
        while que:
            pops = heapq.heappop(que)
            for g in graph[pops[1]]:
                if not g[1] in visited:
                    visited.append(g[1])
                    g[0] += pops[0]
                    heapq.heappush(que, [g[0], g[1]])
        print(graph)
        if set(visited) != set(graph.keys()):
            return -1
        else:
            return max(graph.values())[0][0]


sol = Solution()
answer = sol.networkDelayTime(times=[[1, 2, 1], [2, 3, 2], [1, 3, 4]], n=3, k=1)
# answer = sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
print(answer)
