# not solved

#(3,5)(1,4)(2,4) 
# 앞 숫자가 같거나 뒤 숫자가 같을때는 길이가 적은 것을 선택
# 그냥 단순히 비교할 때는 뒤 숫자로 비교
# 11
# 1 4
# 3 5
# 0 6
# 5 7

number = int(input())
times = []  
count = 1
for i in range(number) : 
    start, end = map(int, input().split())
    times.append((start, end))

for ind, time in enumerate(times) : 
    if ind == 0 : 
        base_start = time[0]
        base_end = time[1]
    else : 
        if base_end < time[0] : 
            base_start = time[0]
            base_end = time[1]
            count += 1
            if time[0] == time[1] : 
                base_start = time[0]
                base_end = time[1]
                count += 1

        elif base_end > time[0] : 
            if base_end < time[1] : 
                continue
            elif base_end > time[1] : 
                base_start = time[0]
                base_end = time[1]

print(count)
