def makeGood(s):
    i = 0
    while s:
        try:
            s[i+1]
        except:
            return s
        else:    
            if s[i].lower() == s[i+1].lower() and (bool(s[i].lower() != s[i]) ^ bool(s[i+1].lower() != s[i+1])):
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i += 1
    return s
        


    

print(makeGood('leEeetcode'))
print(makeGood('abBAcC'))
print(makeGood('s'))