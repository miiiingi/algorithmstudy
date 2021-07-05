def solution(letters, k):
    post_k = len(letters) - k
    answer = [letters[0]]
    for num in letters[1: ] :
        while answer and answer[-1] < num and post_k > 0:
            answer.pop()
            post_k -= 1 
        answer.append(num)
    # 숫자가 깔끔하게 떨어지는 경우
    if post_k == 0 :
        return ''.join(answer)
    # 뒤에 것이 처리되지 못하는 경우
    elif post_k != 0:
        for iter in range(post_k) : 
            answer.pop()
        return ''.join(answer)
# 순서가 이상한데..?
answer = solution('zbgaj', 3)
print(answer)