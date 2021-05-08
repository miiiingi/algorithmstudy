# 각가의 행동들을 어떻게 숫자로 표현할 것인가 ?(C, Z) > 현재 상태 변수, 행동을 시행한 후의 리스트, 삭제된 것을 기억할 리스트 정도 ?
import collections
def solution(n, k, cmd) : 
    cmd = collections.deque(cmd)
    state_current = k
    list_state = ['O' for _ in range(n)]
    list_answer = ['O' for _ in range(n)]
    list_delete = [] # 삭제된 위치를 담는 리스트
    answer = ''
    while cmd : 
        imp = cmd.popleft()
        if len(imp) != 1 :
            command, number = imp.split(' ')
            if command == 'D' : 
                state_current += int(number)
            elif command == 'U' :
                state_current -= int(number)
        elif len(imp) == 1 : 
            command = imp
            if command == 'C' : 
                if state_current == len(list_state)-1 : 
                    del list_state[state_current]
                    list_delete.append(state_current)
                    state_current = len(list_state)-1
                else : 
                    del list_state[state_current]
                    list_delete.append(state_current)
            elif command == 'Z' :
                state_comp = list_delete.pop()
                list_state.append('O')
                if state_comp > state_current : 
                    state_current = state_current
                elif state_comp <= state_current : 
                    state_current += 1
                
    for delete in list_delete : 
        list_answer[delete] = 'X'
    for state in list_answer : 
        answer += state
    return answer 
# answer = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# answer = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
answer = solution(5, 0, ["D 2"])
print(answer)