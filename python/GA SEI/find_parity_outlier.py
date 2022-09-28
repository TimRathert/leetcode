def outlier(nums):        
    if len(list(filter(lambda x : x % 2 == 0, nums))) == 1:
        return list(filter(lambda x : x % 2 == 0, nums))[0]
    else:
        return list(filter(lambda x : x+1 % 2 == 0, nums))[0]

print(outlier([1,3,5,6]))
print(outlier([160, 3, 1719, 19, 11, 13, -21])