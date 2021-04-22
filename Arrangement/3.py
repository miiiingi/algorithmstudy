def solution(citations) : 
    max_comp = max(citations)     
    hindex = [] 
    for comp in range(max_comp+1) : 
        count = 0 
        for citation in citations : 
            if comp <= citation : 
                count += 1
            if comp <= count : 
                hindex.append(comp)
                break
    return max(hindex) 

citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(answer)
#[0,1,3,5,6]
#[6,5,2,2,2]
#[0,3,4,5,6]
#[1,2,10,100,1000]
#[9, 10, 10, 100]
#남은 숫자의 갯수가 현재 숫자보다 크면 따로 리스트로 저장 