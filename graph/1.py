# 모든 숫자의 조합을 다 계산하기는 해야할 듯 ??
# 어떻게 이것들을 반복할 것인가 ?
def solution(numbers, target):
    answer = 0
    def dfs(index):
        nonlocal answer
        if sum(numbers) == target:
            answer += 1
            return
        for ind in range(index, len(numbers)):
            number_minus = numbers[ind]
            del numbers[ind]
            numbers.insert(ind, -number_minus)
            dfs(ind+1)
            del numbers[ind]
            numbers.insert(ind, number_minus)

    dfs(0)
    return answer
answer = solution([1, 1, 1, 1, 1], 3)
print(answer)
# 주효했던 접근은 만약 정답이라면 나머지 경우들을 가지치기 해주는 것! >> return 으로 끝낸다음 원래대로 되돌려주는 것이 유효했다고 생각함
