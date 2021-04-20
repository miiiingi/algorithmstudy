import sys
sys.setrecursionlimit(10000)
def search(width, height, grid) : 
    if width < 0 or width >= len(grid) or height < 0 or height >= len(grid[0]) or grid[width][height] == 0:
        return
    else :  
        grid[width][height] = 0
        search(width-1, height, grid)
        search(width+1, height, grid)
        search(width, height-1, grid)
        search(width, height+1, grid)

countlist = [] 
for testcase in range(int(input())) :
    count = 0
    M, N, bachu = map(int, input().split())
    grid = [[0 for _ in range(N)] for _ in range(M)]
    for number_bachu in range(bachu) :
        v1, v2 = map(int, input().split())
        grid[v1][v2] = 1
    for width in range(M) : 
        for height in range(N) : 
            if grid[width][height] == 0 :
                continue
            else : 
                search(width, height, grid)  
                count += 1
    countlist.append(count)
for i in range(len(countlist)) : 
    print(countlist[i])



