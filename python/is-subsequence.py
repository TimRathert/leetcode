def isSubsequence(s, t):
    sIdx = 0
    if len(s) == 0:
        return True
    for idx, letter in enumerate(t):
        if letter == s[sIdx]:
            sIdx += 1
            if sIdx == len(s):
                return True
    return False      

print(isSubsequence('abc','ahbgdc'))
print(isSubsequence('axc','ahbgdc'))
print(isSubsequence('acb','ahbgdc'))