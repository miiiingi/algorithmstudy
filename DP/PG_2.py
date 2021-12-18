def solution(triangle):
    for length in range(len(triangle))[::-1]:
        for ind in range(len(triangle[length])-1):
            _max = max(triangle[length][ind], triangle[length][ind + 1])
            triangle[length-1][ind] += _max
    return triangle[0][0] 
answer = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
print(answer)
