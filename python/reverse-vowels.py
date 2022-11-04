def reverseVowels(s):
    vowels = {'a':1,'e':1,'i':1,'o':1,'u':1}
    bank = []
    idx = []
    s2 =''
    for index, letter in enumerate(s):
        s2 += letter
        try:
            vowels[letter]
        except:
            continue
        else:
            bank.append(letter)
            idx.append(index)
        while bank:
            s2[idx.pop(0)] = bank[len(bank)-1]
    return s2
    
print(reverseVowels('hello'))
