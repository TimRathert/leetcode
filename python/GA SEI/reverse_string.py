def reverse_string(str):
    output = []
    for letter in str:
        output.insert(0, letter)
    return ''.join(output)

print(reverse_string('abcdefg'))