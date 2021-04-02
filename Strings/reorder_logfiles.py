# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# 풀이방법 생각
# 일단 숫자로그와 문자로그 순서의 차이가 있으므로, 문자로그와 숫자로그를 분류한다.
# 그리고 배열을 정렬해야하는데, key 값을 주어서 정렬하고 싶을 때는 lambda 함수를 써서 정렬을 한다.
# 문자열 다루는 방법 잘 생각해보기 !!
def reorder(strings) : 
    digits = [] 
    letters = [] 
    for string in strings : 
        if string.split()[1].isdigit() :
            digits.append(string)
        else : 
            letters.append(string)
    letters.sort(key = lambda x : (x.split()[1], x.split()[0]))
    return letters + digits
answer = reorder(['dig1 8 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero'])
print(answer)
