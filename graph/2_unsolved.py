def dfs(computers, i, j) : 
    if i < 0 or j < 0 or i >= len(computers) or j >= len(computers) or computers[i][j] == 0 : 
        return 
    computers[i][j] = 0
    dfs(computers, i-1, j)
    dfs(computers, i+1, j)
    dfs(computers, i, j-1)
    dfs(computers, i, j+1)

def solution(n, computers) : 
    result = 0 
    for i in range(len(computers)) : 
        for j in range(len(computers)) : 
            if computers[i][j] == 1 : 
                dfs(computers, i, j)
                result += 1
    return result
answer = solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(answer)