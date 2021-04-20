def dfs(i, j, dangi, count) : 
    if i < 0 or i >= len(dangi) or j < 0 or j >= len(dangi) or dangi[i][j][0] != '1':
        return
    dangi[i][j][0] = '0'
    count += 1
    dfs(i-1, j, dangi, count)  
    dfs(i+1, j, dangi, count)  
    dfs(i, j-1, dangi, count)  
    dfs(i, j+1, dangi, count)  
    return count

N = int(input())
dangi = [[[] for _ in range(N)] for _ in range(N)]
houselist = [] 
for iter in range(N) : 
    for ind, iter2 in enumerate(input()) : 
        dangi[iter][ind].append(iter2)
for i in range(len(dangi)) :
    for j in range(len(dangi[0])) :
        if dangi[i][j][0] == '0' :
            continue
        else : 
            global count 
            count = 0 
            counts = dfs(i, j, dangi, count)
            houselist.append(counts)
print(houselist)