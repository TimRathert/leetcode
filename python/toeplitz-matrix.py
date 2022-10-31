def isToeplitzMatrix(matrix):
    # m = len(matrix)
    # n = len(matrix[0])
    # if m < len(matrix) and n < len(matrix[0]):
    #     if matrix[m][n] != matrix[m+1][n+1]:
    #         return False
    # return True

    i = 0
    while i < len(matrix)-1:
        holder = matrix[i][slice(0, len(matrix[0])-1, 1)]
        compare = matrix[i+1][slice(1, len(matrix[0]), 1)]
        if holder != compare:
            return False
        i += 1
    return True

    # for loop uses more mem than while loop
    # for i in range(len(matrix)-1):
    #     if matrix[i][slice(0, len(matrix[0])-1, 1)]!= matrix[i+1][slice(1, len(matrix[0]), 1)]:
    #         return False
    # return True


        
  # runtime 88ms - faster than 95.34%
  # mem 13.8mb - less than 98.45%          
  # WHOO!



print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitzMatrix([[1,2],[2,2]]))