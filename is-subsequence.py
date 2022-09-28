def isSubsequence(s, t):
    for idx, letter in enumerate(s):
        if letter not in t:
            return False
        

    return all(letter in t for letter in s)

print(isSubsequence('abc','ahbgdc'))
print(isSubsequence('axc','ahbgdc'))
print(isSubsequence('acb','ahbgdc'))