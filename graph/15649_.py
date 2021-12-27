N, M = map(int, input().split())
list_num = [x + 1 for x in range(N)]
result = list()
def dfs(init, numlist, M, visited):
    visited.append(init)
    if len(visited) == M:
        result.append(visited[:])
        visited.pop()
        return
    numlist.remove(init)
    numlist_new = numlist[:]
    for num in numlist_new:
        dfs(num, numlist_new, M, visited)
for num in list_num:
    print(num)
    dfs(num, list_num, M, visited=list())
    list_num.append(num)

