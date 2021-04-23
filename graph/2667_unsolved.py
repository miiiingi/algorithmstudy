N = int(input())
dangi = [[[] for _ in range(N)] for _ in range(N)]
houselist = [] 
for iter in range(N) : 
    for ind, iter2 in enumerate(input()) : 
        dangi[iter][ind].append(iter2)
def apart(dangi) :  
    def dfs(i, j) : 
        if i < 0 or i >= len(dangi) or j < 0 or j >= len(dangi) or dangi[i][j][0] != '1':
            return
        dangi[i][j][0] = '0'
        count  = count + 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    for i in range(len(dangi)) :
        for j in range(len(dangi[0])) :
            if dangi[i][j][0] == '0' :
                continue
            else : 
                count = 0
                # nonlocal count 
                dfs(i, j)
                houselist.append(count)
    return houselist
answer = apart(dangi)
print(answer)