N, M = map(int, input().split())
list_num = [x + 1 for x in range(N)]
result = list()
def dfs(init, numlist, M, visited):
    visited.append(init)
    if len(visited) == M:
        result.append(visited[:])
        return
    numlist_ = numlist[(init - 1) :]
    numlist_.remove(init)
    for num in numlist_:
        dfs(num, numlist_, M, visited)
        visited.pop()
for num in list_num:
    dfs(num, list_num, M, visited=list())
for r in result:
    strs = ""
    for x in r:
        strs += f"{str(x)} "
    strs = strs.strip()
    print(strs)