def checkSubArray(nums, k):
    def recurse():
        sum = 0
        count = 0
        if len(nums) < 2:
            return False
        for num in nums:
            count += 1
            sum += num
            if sum % k == 0 and count > 1:
                return True        
        nums.pop(0)
        return recurse()
    return recurse()

    
#print(checkSubArray([23,2,4,6,7],6))
#print(checkSubArray([5,0,0,0],3))
#print(checkSubArray([0],1))
print(checkSubArray([23,2,4,6,7],6))


