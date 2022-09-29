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

def prime_factors(num):
    if num < 1:
        return "Number must be greater than 1"
    numArr = [num]
    def divider(numArr):
        #print(numArr)
        for val in numArr:
            for factor in range(2,int(val/2), 1):
                #print(factor, val)
                if int(val/2) < 2:
                    pass
                elif (val % factor == 0 and val != factor):
                    numArr.extend((factor, int(val/factor)))
                    numArr.remove(val)
                    divider(numArr)
                    break
    divider(numArr)
    return numArr

        
#print(prime_factors(8))
print(prime_factors(3490))