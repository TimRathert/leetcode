from collections import defaultdict


def groupAnagrams(strs):
    if len(strs) == 0: return []
    letterObj = []
    for word in strs:
        newObj = defaultdict(int)
        for letter in word:
            if not newObj[letter]:
                newObj[letter]= 1
            else: newObj[letter] += 1
        letterObj.append(newObj)
    print(letterObj[0] == letterObj[1])
    return letterObj

print(groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))

            



# first word