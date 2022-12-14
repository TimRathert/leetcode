def phonenum(num):
    return f"({str(num)[0:3]}) {str(num)[3:6]}-{str(num)[6:10]}"

def rgb2hex(r, g, b):
    def tohex(num):
        if num > 255:
            num = 255
        val1 = int((num)/16)
        val2 = int(16*(((num)/16) - int((num)/16)))
        key = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        return f"{key[val1]}{key[val2]}"
    return f"{tohex(r)}{tohex(g)}{tohex(b)}"
