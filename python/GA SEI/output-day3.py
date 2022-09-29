def intersect(list1, list2):
    output = []
    for char in list1:
        try:
            if list2.index(char) != -1:
                output.append(char)
        except:
            pass
    return output

# print(intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']))
#print(intersect(['a', 'b', 'c'], ['x', 'y', 'z']))
#print(intersect(['a', 'b', 'c', 'z'], ['x', 'y', 'z']))

def merge_dictionaries(*data):
    output = {}
    for dict in data:
        #print(len(dict.keys()))
        if dict:
            for key, value in dict.items():
                #print(key, value)
                if key:    
                    try: 
                        output[key] += value
                    except:
                        output[key] = value
    return output   

#print(merge_dictionaries({}, {'a': 1}))
#print(merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}))

# This is mine
# Too clunky tbh. Alyssa's is MUCH more lean. 
def prime_factors(num):
    if num < 1:
        return "Number must be greater than 1"
    numArr = [num]
    def divider(numArr):
        for val in numArr:
            for factor in range(2,int(val/2)+1, 1):
                if int(val/2) < 2:
                    pass
                elif (val % factor == 0 and val != factor):
                    numArr.extend((factor, int(val/factor)))
                    numArr.remove(val)
                    divider(numArr)
                    break
    divider(numArr)
    return numArr

# stole this from Alyssa Wendt
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

print(prime_factors(6154786224))
#print(prime_factors(243))