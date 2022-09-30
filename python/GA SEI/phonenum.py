def phonenum(num):
    return f"({str(num)[0:3]}) {str(num)[3:6]}-{str(num)[6:10]}"

print(phonenum(1234567890))