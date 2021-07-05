def dim_1(answer, dictionary, word) :
    answer.append(word)
    for w in dictionary :
        dim_2(answer, dictionary, word + w)
    return answer
def dim_2(answer, dictionary, word) :
    answer.append(word)
    for w in dictionary :
        dim_3(answer, dictionary, word + w)
def dim_3(answer, dictionary, word) :
    answer.append(word)
    for w in dictionary :
        dim_4(answer, dictionary, word + w)
def dim_4(answer, dictionary, word) :
    answer.append(word)
    for w in dictionary :
        answer.append(word + w)
def solution(word) : 
    answer = [] 
    dictionary = ['A', 'E', 'I', 'O', 'U']
    for dic in dictionary :
        answer = dim_1(answer, dictionary, dic)
    return answer.index(word) + 1
answer = solution('EIO')
print(answer)