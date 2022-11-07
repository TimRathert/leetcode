def maximum69Number(num):
    num = str(num)
    for index,digit in enumerate(num):
        if digit == '6':
            return num[:index] + '9' + num[index+1:]
    return num
    
print(maximum69Number(9669))
print(maximum69Number(9996696))
    