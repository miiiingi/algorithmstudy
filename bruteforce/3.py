# 1. 노란색 카펫을 이루는 조합을 조사한다.
# 2. 갈색 카펫의 갯수를 조사해서 brown이랑 맞는지 비교해본다. # (가로*2) + (세로*2) - 4
# 3. 전체 갯수를 출력한다.
def solution (brown, yellow) : 
    _answer = [] 
    for x in range(yellow) : 
        if (yellow % (x+1)) == 0  : 
            _answer.append(((x+1), (yellow // (x+1))))
    for y in _answer : 
        if y[0] >= y[1] and ((y[0]+2)*2 + (y[1]+2)*2 -4) == brown: 
            return [y[0]+2, y[1]+2]
answer = solution(24, 24)
print(answer)