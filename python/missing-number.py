def missingNumber(nums):
    length = len(nums)
    for i in range(0, len(nums), 1):
        try:
            nums.remove(i)
        except ValueError:
            return i
    return length
        
    
print(missingNumber([0,1,3]))