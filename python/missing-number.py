def missingNumber(nums):
    length = len(nums)
    for i in range(len(nums)):
        try:
            nums.remove(i)
        except ValueError:
            return i
    return length
        
    
print(missingNumber([0,1,3]))