def sums(nums) : 
    numlist = [] 
    nums.sort()
    for i in range(len(nums)) : 
        for j in range((i+1) , len(nums)): 
            for k in range((j+1), len(nums)): 
                if nums[i] + nums[j] + nums[k] == 0 and ([nums[i], nums[j], nums[k]]) not in numlist: 
                    numlist.append(([nums[i], nums[j] , nums[k]]))
    return numlist

def sums2(nums) : 
    numlist = [] 
    nums.sort()
    for i in range(len(nums)-2) :  
        if nums[i] == nums[i-1] :
            continue
        left, right = (i+1) , len(nums)
        if (nums[i] + nums[left] + nums[right-1]) < 0 : 
            for j in range(left+1, len(nums)) : 
                if (nums[i] + nums[j] + nums[right-1]) == 0 : 
                    numlist.append([nums[i], nums[j], nums[right-1]])
        elif (nums[i] + nums[left] + nums[right-1]) > 0 :
             for j in range(left+1, len(nums), -1) : 
                if (nums[i] + nums[j] + nums[right-1]) == 0 : 
                    numlist.append([nums[i], nums[j], nums[right-1]])           
        elif (nums[i] + nums[left] + nums[right-1]) == 0 :
            numlist.append([nums[i], nums[j], nums[right-1]])           


    return numlist

answer = sums([-1, 0, 1, 2, -1, -4])
answer2 = sums2([-1, 0, 1, 2, -1, -4])

print(answer2)