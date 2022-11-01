from collections import defaultdict


def groupAnagrams(strs):
    if len(strs) == 0: return []
    letterObj = {}
    seen = defaultdict(dict)
    output = []
    var = 0
    for word in strs:

        newObj = defaultdict(dict)
        # using defaultdict prevents python from returning a keyerror if the key doesn't exist within that object (useful on line 23)

        for letter in word:
            if not newObj[letter]:
                newObj[letter] = 1
            else: newObj[letter] += 1
        newObj = frozenset(newObj.items())
        # for each of the words in strs, a newObj is created
        # the keys are the letters and the values are the number of times that letter appears

        if not seen[newObj]: #if seen[newObj] doesn't exist, create it
                            # this uses the key value pairs from newObj (containing letter frequency) as the key and True as the value
            seen[newObj] = True
            letterObj[newObj] = var  #var is the counter. I used this to track the index of the corresponding word in the output array
            var += 1 # when a word is inserted, this increments to denote where the next item will be inserted
            output.append([word])
        elif seen[newObj]: #if line 23 is false (aka it already exists) then the index is read from letterObj[newObj] = var to determine where to insert the current word in the output array
            keys = seen.keys() #not sure I need this...
            output[letterObj[newObj]].append(word)


    return output

            

print(groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))
#print(groupAnagrams(["ddddddddddg","dgggggggggg"]))
            



# first word


# def groupAnagrams(strs):
#     if len(strs) == 0: return []
#     letterObj = {}
#     seen = defaultdict(int)
#     output = []
#     var = 0
#     for word in strs:
#         newObj = defaultdict(int)
#         for letter in word:
#             if not newObj[letter]:
#                 newObj[letter]= 1
#             else: newObj[letter] += 1
#         if not seen[frozenset(newObj)]:
#             seen[frozenset(newObj)] = True
#             letterObj[frozenset(newObj)] = var
#             var += 1
#             output.append([word])
#         elif seen[frozenset(newObj)]:
#             keys = seen.keys()
#             output[letterObj[frozenset(newObj)]].append(word)