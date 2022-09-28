def even_range(start, end):
    arr = []
    for num in range(start, end, 1):
        if num % 2 == 0:
            arr.append(num)
    return arr
    
print(even_range(2,11))