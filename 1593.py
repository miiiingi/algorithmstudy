g, s = map(int, input().split())
W = input()
S = input()
answer = 0 
length = 0 
answer_list = [0] * 52
compared_list = [0] * 52
for w in W : 
    if 'a' <= w and w <= 'z' : 
        answer_list[ord(w) - 97] += 1
    elif 'A' <= w and w <= 'Z' : 
        answer_list[ord(w) - 39] += 1
for ind in range(s) : 
    if 'a' <= S[ind] and S[ind] <= 'z' : 
        compared_list[ord(S[ind]) - 97] += 1
    elif 'A' <= S[ind] and S[ind] <= 'Z' : 
        compared_list[ord(S[ind]) - 39] += 1
    # print(compared_list)
    length += 1
    if length == g : 
        if answer_list == compared_list : 
            answer += 1
        if 'a' <= S[ind - (g-1)] and S[ind - (g-1)] <= 'z' : 
            compared_list[ord(S[ind - (g - 1)]) - 97] -= 1
        elif 'A' <= S[ind - (g-1)] and S[ind - (g-1)] <= 'Z' : 
            compared_list[ord(S[ind - (g - 1)]) - 39] -= 1
        # print(compared_list)
        length -= 1
print(answer)
