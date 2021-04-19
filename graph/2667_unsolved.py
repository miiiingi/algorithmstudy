def dfs(i, j, dangi, house) : 
    if i < 0 or i >= len(dangi) or j < 0 or j >= len(dangi) or dangi[i][j][0] != '1':
        return
    dangi[i][j][0] = '0'
    house += 1
    dfs(i-1, j, dangi, house)  
    dfs(i+1, j, dangi, house)  
    dfs(i, j-1, dangi, house)  
    dfs(i, j+1, dangi, house)  
    return house

N = int(input())
dangi = [[[] for _ in range(N)] for _ in range(N)]
count = 0
houselist = [] 
for iter in range(N) : 
    for ind, iter2 in enumerate(input()) : 
        dangi[iter][ind].append(iter2)
for i in range(len(dangi)) :
    for j in range(len(dangi[0])) :
        if dangi[i][j][0] == '0' :
            pass
        else : 
            house = 0 
            count_house = dfs(i, j, dangi, house)
            houselist.append(count_house)
            count += 1
print(count, houselist)