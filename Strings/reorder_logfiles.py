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
