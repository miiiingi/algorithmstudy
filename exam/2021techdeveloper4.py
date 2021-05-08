import collections
def solution(places) : 
    answer = [] 
    places = collections.deque(places)
    while places : 
        grid = [[[] for _ in range(5)] for _ in range(5)]
        place = places.popleft()
        condition = True 
        count  = 0 
        for i in range(5) : 
            for j in range(5) : 
                grid[i][j] = place[i][j]
        def parallel(i, j, direction) : 
            if i < 0 or i >= 5 or j < 0 or j >= 5 :
                return
            if direction == 0 :
                if grid[i][j] == 'P' and grid[i+1][j] == 'O' or grid[i+1][j] == 'P' :
                        return False
            if direction == 1 :
                if grid[i][j] == 'P' and grid[i-1][j] == 'O' or grid[i-1][j] == 'P' :
                        
                        return False
            if direction == 2 :
                if grid[i][j] == 'P' and grid[i][j+1] == 'O' or grid[i][j+1] == 'P' :
                        return False

            if direction == 3 :
                if grid[i][j] == 'P' and grid[i][j-1] == 'O' or grid[i][j-1] == 'P' :
                        return False

        def daegak(i, j, direction) : 
            if i < 0 or i >= 5 or j < 0 or j >= 5 :
                return
            if direction == 0 :
                if grid[i][j] == 'P': 
                    if grid[i][j+1] == 'O' or grid[i+1][j] == 'O' :
                        return False
            if direction == 1 :
                if grid[i][j] == 'P': 
                    if grid[i][j-1] == 'O' or grid[i+1][j] == 'O' :
                        return False

            if direction == 2 :
                if grid[i][j] == 'P': 
                    if grid[i-1][j] == 'O' or grid[i][j+1] == 'O' :
                        return False
            if direction == 3 :
                if grid[i][j] == 'P': 
                    if grid[i][j-1] == 'O' or grid[i-1][j] == 'O' :
                        return False
       
        def dfs(i, j) : 
            if i < 0 or i >= 5 or j < 0 or j >= 5 :
                return
            condition = parallel(i-2, j, 0) # 0 : 가로 방향 마이너스 , 1 : 가로 방향 플러스
            if condition == False : 
                return False
            condition =parallel(i+2, j, 1)
            if condition == False : 
                return False
            condition =parallel(i, j-2, 2) # 2 : 세로 방향 마이너스, 3 : 세로 방향 플러스
            if condition == False : 
                return False
            condition =parallel(i, j+2, 3)
            if condition == False : 
                return False
            condition =daegak(i-1, j-1, 0)
            if condition == False : 
                return False
            condition =daegak(i-1, j+1, 1)
            if condition == False : 
                return False
            condition =daegak(i+1, j-1, 2)
            if condition == False : 
                return False
            condition =daegak(i+1, j+1, 3)
            if condition == False : 
                return False

        for i in range(5) :
            for j in range(5) : 
                if grid[i][j] == 'P' :
                    condition = dfs(i, j)
                    if condition == False:
                        count += 1 
                        break
        if count != 0 : 
            answer.append(0)
        else : 
            answer.append(1)
    return answer
answer = solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
print(answer)