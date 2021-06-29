# 이동반경 제한
# 알파벳 변환 순서 고려
# 기준점을 어떻게 다시 정할 것인가?
# 어떻게 탐색하는 시간 줄일 것인가 ? >> 조금 더 greedy한 방법으로 ??

def search_loc(name, loc):
    for ind in range(loc, len(name)):
        if name[ind] != "A":
            min_right = ind
            break
    for ind in range(loc, -len(name), -1):
        if name[ind] != "A":
            min_left = ind
            break

    min_right_ = min_right - loc
    min_left_ = loc - min_left
    if min_right_ <= min_left_:
        return min_right_, True
    else:
        return min_left_, False


def search_num(name, num):
    num_to_z = ord("Z") - ord(name[num])
    num_to_a = ord(name[num]) - ord("A")
    if num_to_a <= num_to_z:
        return num_to_a
    else:
        return num_to_z + 1


def solution(name):
    answer = 0
    start_num = 0
    start_cha = "A" * len(name)
    while True:
        answer += search_num(name, start_num)  # 알파벳 변환 순서 고려
        if start_num != -1:
            name = name[:start_num] + "A" + name[start_num + 1 :]
        else:
            name = name[:start_num] + "A"
        if name == start_cha:
            break
        else:
            loc_min, right = search_loc(name, start_num)
            answer += loc_min
            if right:
                start_num += loc_min
            else:
                start_num -= loc_min
    return answer


answer = solution("ABAAAAAAAAABB")
print(answer)
