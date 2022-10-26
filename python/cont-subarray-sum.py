# def checkSubArray(nums, k):
#     def recurse():
#         sum = 0
#         count = 0
#         if len(nums) < 2:
#             return False
#         for num in nums:
#             count += 1
#             sum += num
#             if sum % k == 0 and count > 1:
#                 return True        
#         nums.pop(0)
#         return recurse()
#     return recurse()
# this works, but times out on leetcode. RIP

def checkSubArray(nums, k):
    hashmap = {0: 0}
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s % k not in hashmap:
            hashmap[s % k] = i + 1
        elif hashmap[s % k] < i:
            return True

#print(checkSubArray([23,2,4,6,7],6))
#print(checkSubArray([5,0,0,0],3))
#print(checkSubArray([0],1))
print(checkSubArray([23,2,4,6,7],6))


