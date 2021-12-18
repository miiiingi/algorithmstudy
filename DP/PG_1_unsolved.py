def solution(N, number) : 
    length = len(str(number))
    comp = str(N) * length
    cnt = 2
    while(True) : 
        comp_ = int(comp)
        diff_times = abs(comp_ - (number * N))
        diff_plus = abs(comp_ - (number + N))
        diff_minus = abs(comp_ - (number - N))
        if min(diff_times, diff_plus, diff_minus) == diff_times : 
            number *= N
        elif min(diff_times, diff_plus, diff_minus) == diff_plus : 
            number += N
        elif min(diff_times, diff_plus, diff_minus) == diff_minus : 
            number -= N
        cnt += 1
        if cnt > 8 :
            return -1
        if str(number) == comp : 
            return cnt
answer = solution(2, 11)
print(answer)
