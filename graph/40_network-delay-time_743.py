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
        return max(self.count)
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


# answer = Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1], [1, 5, 3]], 5 ,2)
answer = Solution().networkDelayTime([[1,2,1]], 2 ,1)

print(answer)
