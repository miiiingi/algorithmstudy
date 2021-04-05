def solution(citations) : 
    num_max = 0 
    num_list = [] 
    citations = sorted(citations, reverse= True)
    for ind, x in enumerate(citations) : 
        if (ind+1) >= x : 
            num_list.append(x)
        # length = (_length - ind)
        # if x <= length and x >= num_max : 
        #     num_max = x
    if len(num_list) != 0 : 
        num_max = max(num_list)
    return num_max 
citations = [2,2,2,5,6]
answer = solution(citations)
print(answer)
#[0,1,3,5,6]
#[6,5,2,2,2]
#[0,3,4,5,6]
#[1,2,10,100,1000]
#[9, 10, 10, 100]
#남은 숫자의 갯수가 현재 숫자보다 크면 따로 리스트로 저장 