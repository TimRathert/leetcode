from collections import defaultdict

def longestPalindrome(words):
    unpaired = output = 0
    needPair = defaultdict(int)
    for item in words:
        if item[0] == item[1]:
            if needPair[item] > 0:
                unpaired -= 1
                needPair[item] -= 1
                output += 4
            else:
                needPair[item] += 1
                unpaired += 1
        else:
            if needPair[item[::-1]] > 0:
                output += 4
                needPair[item[::-1]] -= 1
            else:
                needPair[item] += 1
    if unpaired > 0: output += 2
    return output
        
        



print(longestPalindrome(["lc","cl","gg"])) 
print(longestPalindrome(["ab","ty","yt","lc","cl","ab"])) 
print(longestPalindrome(["cc","ll","xx"])) 
print(longestPalindrome(["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"])) 

["qo","fo","ff","qq","qf","of","oo","of","of","qf","qf","of"]
