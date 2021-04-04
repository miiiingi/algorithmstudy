# 문제
# 동전을 적적히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전의 갯수의 최솟값을 구해라.

A, B = input().split()
A, B = int(A), int(B)
coinlist = [] 
count = 0
for i in range(A) : 
    coinlist.append(int(input()))
for x in coinlist[::-1] :  
    if x <= B : 
        mok = B // x
        count += mok
        B -= x * mok
        if B == 0 : 
            break
print(count)

