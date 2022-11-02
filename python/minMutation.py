def minMutation(start, end, bank):
    diffObj = {}
    totalChanges = 0
    if len(bank) == 0 and start != end:
        return -1
    for index, letter in enumerate(start):
        if letter != end[index]:
            totalChanges += 1
    for index, word in enumerate(bank):
        startDiff = 0
        endDiff = 0
        for idx, letter, in enumerate(word):
            if letter != start[idx]:
                startDiff += 1
            if letter != end[idx]:
                endDiff += 1
            print(index, idx, startDiff, endDiff)
        diffObj[startDiff] = {'endDiff': endDiff, 'index': index}
    if len(bank) == 1 and diffObj[1]['endDiff'] == 0:
        return 1
    print(diffObj)
    countdownVar = diffObj[1]['endDiff']
    minMut = len(bank)
    for i in range(1, len(bank), 1):
        try:
            diffObj[i]
        except:
            return -1
        
        else: 
            if diffObj[i]['endDiff'] == 0 and i < minMut:
                minMut = i
            if bank[i-1] == end and i > totalChanges:
                return i

            if diffObj[i]['endDiff'] > countdownVar:
                return -1


    return minMut



#print(minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"]))
#print(minMutation("AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))
#print(minMutation("AAAAACCC","AACCCCCC",["AAAACCCC","AAACCCCC","AACCCCCC"]))
#print(minMutation("AACCTTGG","AATTCCGG",["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))
#print(minMutation("AACCGGTT","AACCGGTA",[]))
#print(minMutation("AACCGGTT","AACCGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(minMutation("AACCGGTT","AAACGGTA",["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))

