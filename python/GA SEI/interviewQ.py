def stairs(arr):
    low = 0
    current = 0
    for num in arr:
        current += num        
        if current < low:
            low = current
    print(f"Monkey should start on stair {1-low}") 

stairs([1,-3,-4,8,2])
stairs([2,-6,9,4,-2,-7,-11])
stairs([-1])

