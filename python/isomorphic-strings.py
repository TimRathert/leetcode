def isIsomorphic(s, t):
    arr = []
    splaceArr = []
    tplaceArr = []
    for letter in s:
        if letter in arr:
            pass
        else:
            arr.append(letter)
        splaceArr.append(arr.index(letter))
    arr = []
    for letter in t:
        if letter in arr:
            pass
        else:
            arr.append(letter)
        tplaceArr.append(arr.index(letter))
    return splaceArr == tplaceArr

print(isIsomorphic('egg','add'))
print(isIsomorphic('foo','bar'))
print(isIsomorphic('paper','title'))

    