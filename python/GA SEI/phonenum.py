def phonenum(num):
    a = "".join(str(x) for x in num[0:3])
    b = "".join(str(x) for x in num[3:6])
    c = "".join(str(x) for x in num[6:10])
    return f"({a}) {b}-{c}"


print(phonenum([1,2,3,4,5,6,7,8,9,0]))