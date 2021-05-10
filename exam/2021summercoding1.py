import collections
def solution(code, day, data):
    answer = []
    answer_int = [] 
    data = collections.deque(data)
    while data:
        price, data_code, time = data.popleft().split(" ")
        if data_code[5:] == code and time[5:13] == day:
            answer.append((price, time[5:]))
    answer.sort(key = lambda x : x[1])
    for a in answer : 
        answer_int.append(int(a[0][6:]))
    return answer_int


answer = solution(
    "012345",
    "20190620",
    [
        "price=80 code=987654 time=2019062113",
        "price=90 code=012345 time=2019062014",
        "price=120 code=987654 time=2019062010",
        "price=110 code=012345 time=2019062009",
        "price=95 code=012345 time=2019062111",
    ],
)
print(answer)
