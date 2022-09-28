def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return float('nan')
    count = 0
    for idx, char in enumerate(str1):
        if str2[idx] != char:
            count += 1
    return count

print(hamming_distance('abc', 'abc'))
print(hamming_distance('a1c', 'a2c'))
print(hamming_distance('!!!!', '****'))
print(hamming_distance('abc', 'ab'))