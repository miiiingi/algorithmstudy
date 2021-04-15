# 일단, 길이가 3인 리스트를 n*n갯수 만큼 만들어서 모든 길을 초기화
# 움직이는 것을 어떻게 코드로 표현할 것 인가?
def solution(n, z, roads, queries) : 
    answer = [] 
    state = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) : 
        for j in range(n) :
            if i == j :
                state[i][j] = z
            elif i != j : 
                for road in roads : 
                    if road[0] == i and road[1] == j :
                        state[i][j] = road[2]
    for iter in range(len(queries)) : 
        curr = 0 
        if queries[iter] == 0 :
            answer.append(0)
            continue
        else : 
            while True :
                rewardlist = [] 
                stack = 0
                for ind, reward in enumerate(state[curr]) : 
                    if reward > queries[iter] :  
                        answer.append(-1)
                        break
                    elif reward < queries[iter] : 
                        rewardlist.append((ind, reward))
                reward_high = max(rewardlist)

    return answer
answer = solution(5, 5, [[1,2,3],[0,3,2]], [0,1,2,3,4,5,6])
print(answer)
