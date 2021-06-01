n = int(input())
array = [] 
for number in map(int,input().split()) : 
    array.append(number)
target = int(input())
array.sort()
answer = 0 
start = 0 
end = n-1 
while start < end : 
    if array[start] + array[end] < target : 
        start += 1
    elif array[start] + array[end] > target : 
        end -= 1
    else : 
        start += 1
        end -= 1
        answer += 1
print(answer)
    
    
    

