# 효율성이 왜 터지지 ??
def binary(array, target) : 
    low = 0 
    upper = len(array) - 1 
    index = -1 
    while low <= upper : 
        middle = (low + upper) // 2
        if array[middle] == target : 
            index = middle
            return index
        elif array[middle] < target : 
            upper = array[middle]
        elif array[middle] > target :
            low = array[middle]
    return index
answer = binary([2,5,7,9,11], 4)
print(answer)