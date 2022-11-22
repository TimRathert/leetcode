# perfect squares: 1, 4, 9, 16, 25, 36, 49, etc...
# define perfect squares
# find the shortest path from n to 0 using only perfect squares
# count the steps 
# return steps


# iterate from 2:
# is n less than 4?
    # n = n - 1
    # squares.append(1)
# is n > i^2?
    #  n = n - i^2
    # squares.append(i^2)
# start over from 2:


def numSquares(n):
    if n < 2:
        return n
    list = []
    i = 1
    while i * i <= n:
        list.append( i * i )
        i += 1
    count = 0
    toCheck = { n }
    while toCheck:
        count += 1
        temp = set()
        for x in toCheck:
            for y in list:
                if x == y:
                    return count
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp
    return count

print(numSquares(13))
