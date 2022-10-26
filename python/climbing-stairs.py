# 2 > 2 options
# 3 > 3 options
# 4 > 5 options
# 5 > 8 options 
# 6 > 13 options
# fibonacci!

# 3//2 = 1
# 3%2 = 1

# def climbStairs(n):
#     steps = 0 #unneccessary
#     arr = [1,1]
#     for idx,num in enumerate(range(2, n+1)):
#         arr.append(arr[num-1]+arr[num-2])
#     return arr[-1]

def climbStairs(n):
    arr = [1,1]
    def recurse():
        arr.append(arr[len(arr)-1]+arr[len(arr)-2])
    while len(arr) < n+1:
        recurse()
    return arr[-1]
    

print(climbStairs(6))