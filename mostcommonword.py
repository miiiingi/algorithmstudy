# 문제
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

# 전략
# 1. 일단 특수문자를 제외한 단어를 분리하고, 대문자를 소문자로 바꾸어 둘 간의 차이를 없애준다.
# 2. 등장하는 단어의 숫자를 센다.

import collections
import re

def common(strings, banned) : 
    _strings = [re.sub('[^\w]', '', s.lower()) for s in strings.split() if banned[0] not in s]
    for item in collections.Counter(_strings).items() :
        if item[1] == max(collections.Counter(_strings).values()) : 
            return item[0] 

def common2(strings, banned) : 
    _strings = [re.sub('[^\w]', '', s.lower()) for s in strings.split() if banned[0] not in s]
    counts = collections.Counter(_strings) 
    return counts.most_common(1)[0][0]

strings = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']
answer = common(strings, banned)
answer2 = common2(strings, banned)
