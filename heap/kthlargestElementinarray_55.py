# 문제
# 정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
def solution(L, x):
    for ind in range(len(L)) :
        if ind == 0 and x <= L[ind] : 
            L.insert(ind, x)
       	elif ind > 0 and L[ind-1] <= x < L[ind] : 
            L.insert(ind, x)
            break
       	elif ind == len(L) - 1 and x >= L[ind] : 
            L.insert(ind, x)                      
    return L
answer = solution([20, 37, 58, 72, 91], 65)
print(answer)