def solution(n, computers) : 
    result = 0 
    def dfs(coordinate) : 
        if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] >= len(computers) or coordinate[1] >= len(computers) or computers[coordinate[0]][coordinate[1]] == 0 : 
            return 
        computers[coordinate[0]][coordinate[1]] = 0
        dfs([coordinate[0]-1, coordinate[1]])
        dfs([coordinate[0]+1, coordinate[1]])
        dfs([coordinate[0], coordinate[1]-1])
        dfs([coordinate[0], coordinate[1]+1])

    for i in range(len(computers)) : 
        for j in range(len(computers)) : 
            if computers[i][j] == 0 : 
                continue
            dfs([i, j])
            result += 1
    return result
answer = solution(3, [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# answer = solution(2, [[1, 1],[1,0]])
print(answer)