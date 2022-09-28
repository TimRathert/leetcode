def phrase_finder(words, phrase):
    for phword in phrase.split(' '):
        if phword not in words:
            return False
    return True


print(phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye'))