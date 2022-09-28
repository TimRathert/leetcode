# 2 > 2 options
# 3 > 3 options
# 4 > 5 options
# 5 > 8 options 
# 6 > 13 options
# fibonacci!

# 3//2 = 1
# 3%2 = 1

def climbStairs(n):
    steps = 0
    arr = [1,1]
    for idx,num in enumerate(range(2, n+1)):
        arr.append(arr[num-1]+arr[num-2])
    return arr[-1]

print(climbStairs(6))