# 문제
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

# 전략
# 1. 단어가 같은 그룹인지를 구별
# 2. 같은 그룹이라면 같은 그룹으로 묶일 수 있도록 정리

def group(strings) : 
    strings_ = [''.join(sorted(x)) for x in strings]
    print(strings_)
    
group(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])