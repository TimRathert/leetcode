def longestPalindrome(words):
    copyPasta = words
    needPair = {'dupes':[]}
    output = 0
    for index, item in enumerate(words):
        needPair[item] = index
    for i in range(len(words)-1):      
        try:
            needPair[item[::-1]]
        except:
            None
        else:
           
            #print(index, item)
    #print(needPair)
    for item in needPair:
        if item[0] == item[1]:
            needPair.pop(item)
            output += 2
            break
    return output



#print(longestPalindrome(["lc","cl","gg"])) 
#print(longestPalindrome(["ab","ty","yt","lc","cl","ab"])) 
#print(longestPalindrome(["cc","ll","xx"])) 
print(longestPalindrome(["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"])) 

