import collections
def solution(routes) : 
    routes = collections.deque(sorted(routes, key = lambda x : (x[1]-x[0])))
    answer = 0 
    while routes : 
        answer += 1
        route = routes.popleft()
        list_out = []
        for ind in range(len(routes)) : 
            if routes[ind][0] <= route[0] <= routes[ind][1] or routes[ind][0] <= route[1] <= routes[ind][1] : 
                list_out.append(routes[ind])
        for out in list_out : 
            routes.remove(out)
    return answer
answer = solution([[0,2],[2,3],[3,4],[4,6]])
print(answer)