from collections import defaultdict


def groupAnagrams(strs):
    if len(strs) == 0: return []
    letterObj = []
    seen = defaultdict(dict)
    output = []
    for word in strs:
        newObj = defaultdict(int)
        for letter in word:
            if not newObj[letter]:
                newObj[letter]= 1
            else: newObj[letter] += 1
        letterObj.append(newObj)
        if not seen[frozenset(newObj)]:
            seen[frozenset(newObj)] = True
            output.append([word])
        if seen[frozenset(newObj)]:
            output[seen.keys(frozenset(newObj))]


    return output

            

print(groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))

            



# first word