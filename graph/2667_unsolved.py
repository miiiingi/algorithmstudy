def dfs(i, j, dangi, house = 0) : 
    if i < 0 or i >= len(dangi) or j < 0 or j >= len(dangi) or dangi[i][j][0] != '1':
        return
    dangi[i][j][0] = '0'
    house += 1
    house = dfs(i-1, j, dangi, house)  
    house = dfs(i+1, j, dangi, house)  
    house = dfs(i, j-1, dangi, house)  
    house = dfs(i, j+1, dangi, house)  
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
            continue
        else : 
            count_house = dfs(i, j, dangi)
            houselist.append(count_house)
            count += 1
print(count, houselist)