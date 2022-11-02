def minMutation(start, end, bank):
    difference = {}
    for idx, letter in enumerate(start):
        if letter != end[idx]:
            difference[idx] = end[idx]



print(minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"])
print(minMutation("AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"])
print(minMutation("AAAAACCC","AACCCCCC",["AAAACCCC","AAACCCCC","AACCCCCC"])

#