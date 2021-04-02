# 문제
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

# 풀이방법 생각
# 그냥 인덱스 뒤집어서 리스트에 붙이기 ?

def reverse(strings) : 
    answer = [] 
    for x in strings[::-1] : 
        answer.append(x)
    return answer
answer = reverse(['h','e','l','l','o'])
print(answer)
