import collections
from types import coroutine
testcase = int(input())
for iter in range(testcase) : 
    length = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    check = [[1 for _ in range(length)] for _ in range(length)]
    answer = 0 
    def bfs(check, i, j) : 
        discovered = [(i, j)] 
        queue = collections.deque([(i, j)])
        while queue : 
            Q = queue.popleft()
            candidate = [(Q[0]-2, Q[1]-1), (Q[0]-2, Q[1]+1), (Q[0]-1, Q[1]-2), (Q[0]-1, Q[1]+2), (Q[0]+2, Q[1]-1), (Q[0]+2, Q[1]+1), (Q[0]+1, Q[1]-2), (Q[0]+1, Q[1]+2)]
            for coor in candidate : 
                if (coor[0], coor[1]) == (end_x, end_y) : 
                    answer = check[end_x][end_y]
                    break
                if coor[0] < 0 or coor[1] < 0 or coor[0] >= length or coor[1] >= length or check[coor[0]][coor[1]] != 1 or (coor[0], coor[1]) == (start_x, start_y) : 
                    continue
                check[coor[0]][coor[1]] += check[Q[0]][Q[1]] 
                queue.append((coor[0], coor[1]))
    bfs(check, start_x, start_y)
    if answer != 0 : 
        print(answer-1)
    else : 
        print(answer)