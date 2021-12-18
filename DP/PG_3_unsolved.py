def house(paths, path, m, n, puddles):
    path_x = path[0]
    path_y = path[1]
    if path_x > m or path_y > n or path == puddles[0]:
        return
    else:
        return paths.append(path)
def solution(m, n, puddles):
    import collections
    paths = collections.deque([[1, 1]])
    result = list()
    while paths:
        p = paths.popleft()
        if p == [m, n]:
            result.append(p)
        else:
            house(paths, [p[0] + 1, p[1]], m, n, puddles)
            house(paths, [p[0], p[1] + 1], m, n, puddles)
    return len(result) 
answer = solution(4, 3, [[2, 2]])
print(answer)

