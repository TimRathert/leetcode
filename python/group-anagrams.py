from collections import defaultdict


def groupAnagrams(strs):
    if len(strs) == 0: return []
    letterObj = {}
    seen = defaultdict(dict)
    output = []
    var = 0
    for word in strs:
        newObj = defaultdict(dict)
        for letter in word:
            if not newObj[letter]:
                newObj[letter] = 1
            else: newObj[letter] += 1
        newObj = frozenset(newObj.items())
        if not seen[newObj]:
            seen[newObj] = True
            letterObj[newObj] = var
            var += 1
            output.append([word])
        elif seen[newObj]:
            keys = seen.keys()
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