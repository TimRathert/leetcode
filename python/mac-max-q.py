from jinja2 import Undefined
from numpy import sort


def rearranged(int):
    low1 = Undefined
    low2 = Undefined
    for num in int:
        if low1 == Undefined:
            low1 = num
        elif low2 == Undefined:
            low2 = num
        elif num < low1 or num < low2:
            if low1 > low2:
                if num < low1:
                    low1 = num
            elif low2 > low1:
                if num < low2:
                    low2 = num
    int.remove(low1)
    int.remove(low2)
    int.sort()
    int.insert(2,low1)
    if len(int) % 2 == 0:
        int.insert(len(int),low2)
    else:
        int.insert(len(int)-1,low2)
    return int
        
print(rearranged([21, 34, 5, 7, 9]))
#print(rearranged([21, 34, 5, 7, 9, 15, 72, 4]))

    # U = 1
    # for index, num in enumerate(int):
    #     if index < 2:
    #         U *= num
    #     elif index == 2:
    #         U /= num
    #     elif index == len(int)-1:
    #         if index % 2 == 1:
    #             U /= num
    #         if index %2 == 0:
    #             U *= num

