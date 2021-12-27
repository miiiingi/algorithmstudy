N, M = map(int, input().split())
list_num = [x + 1 for x in range(N)]
result = list()


def dfs(init, numlist, M, visited):
    visited.append(init)
    if len(visited) == M:
        result.append(visited[:])
        return
    numlist_ = numlist[:]
    numlist_.remove(init)
    numlist_new = numlist_[:]
    for num in numlist_new:
        dfs(num, numlist_new, M, visited)
        visited.pop()


for num in list_num:
    dfs(num, list_num, M, visited=list())

