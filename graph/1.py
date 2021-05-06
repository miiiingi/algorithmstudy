# 모든 숫자의 조합을 다 계산하기는 해야할 듯 ??
# 어떻게 이것들을 반복할 것인가 ? 
def solution(numbers, target) : 
    answer = 0 
    def dfs(index) : 
        if sum(numbers) == target : 
            answer += 1
            return
        pass
    dfs(0)
    return answer 
answer = solution([1,1,1,1,1], 3)
print(answer)