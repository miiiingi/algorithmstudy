# 이동반경 제한
# 알파벳 변환 순서 고려
# 기준점을 어떻게 다시 정할 것인가?

# 어떻게 탐색하는 시간 줄일 것인가 ? >> 조금 더 greedy한 방법으로 ??
def search_loc(name, loc) : 
    loc_left = loc
    loc_right = loc
    while True :
        if loc_right >= len(name) : 
            return
        if name[loc_right] != 'A' :
            min_right = loc_right 
            break
        else : 
            loc_right += 1

    while True :
        if -len(name) >= loc_left :
            return
        if name[loc_left] != 'A' :
            min_left = loc_left 
            break
        else : 
            loc_left -= 1
    min_right_ = (min_right - loc)
    min_left_ = (loc - min_left)
    if min_right_ <= min_left_ :
        return min_right_, True
    else : 
        return min_left_, False

def search_num(name, num) :
    num_to_z = ord('Z') - ord(name[num])
    num_to_a = ord(name[num]) - ord('A')
    if num_to_a <= num_to_z :
        return num_to_a
    else : 
        return num_to_z + 1

def solution(name) :
    answer = 0 
    start_num = 0
    start_cha = 'A' * len(name)
    while not start_cha == name : 
        if name[start_num] == 'A' :
            pass
        else : 
            answer += search_num(name, start_num) # 알파벳 변환 순서 고려
            if start_num >= 0 :
                name = name[:start_num] + 'A' + name[start_num+1: ]
            else : 
                name = name[:start_num] + 'A'
            try : 
                loc_min, right = search_loc(name, start_num)
                answer += loc_min
                if right : 
                    start_num += loc_min
                else : 
                    start_num -= loc_min
            except : 
                pass
    return answer
answer = solution('JEROEN')
print(answer)
