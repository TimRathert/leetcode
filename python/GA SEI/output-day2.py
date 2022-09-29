# warmup
def reverse_string(str):
    output = []
    for letter in str:
        output.insert(0, letter)
    return ''.join(output)

#0
def isPrime(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    return True

#1
def outlier(nums):        
    if len(list(filter(lambda x : x % 2 == 0, nums))) == 1:
        return list(filter(lambda x : x % 2 == 0, nums))[0]
    else:
        return list(filter(lambda x : x+1 % 2 == 0, nums))[0]