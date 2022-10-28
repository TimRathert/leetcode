def largestOverlap(img1, img2):
    emptyRow = []
    def bigbigly():
        for i in range(0, len(img2)**2, 1):
            emptyRow.append(0)

        for i in range(0, len(img2), 1):
            for j in range(0, len(img2), 1):
                img1[i].append(0)
                img1[i].insert(0 , 0)

        for i in range(0, len(img2), 1):
            img1.insert(0, emptyRow)    
            img1.append(emptyRow)
    bigbigly()
    print(img1)
    count = []
    for xaxis in range(-(len(img2)),len(img2)*2, 1): 
        for yaxis in range(-(len(img2)),len(img2)*2, 1):
            overlap = 0
            for idx, array in enumerate(img2):
                i2 = idx
                for index,item in enumerate(array):
                    j2 = index

                    if img1[len(img2)+yaxis][len(img2)+ xaxis] + img2[i2][j2] == 2:
                        overlap += 1
            count.append(overlap)
    return max(count)

# runs and WORKS but time complexity is too high. Too many loops. Should probably consolidate them.

#print(largestOverlap( [[1,1,0],[0,1,0],[0,1,0]],[[0,0,0],[0,1,1],[0,0,1]]))
print(largestOverlap([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]))


#solution stolen from leetcode

# class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

#         dim = len(A)

#         def shift_and_count(x_shift, y_shift, M, R):
#             """ 
#                 Shift the matrix M in up-left and up-right directions 
#                   and count the ones in the overlapping zone.
#                 M: matrix to be moved
#                 R: matrix for reference

#                 moving one matrix up is equivalent to
#                 moving the other matrix down
#             """
#             left_shift_count, right_shift_count = 0, 0
#             for r_row, m_row in enumerate(range(y_shift, dim)):
#                 for r_col, m_col in enumerate(range(x_shift, dim)):
#                     if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
#                         left_shift_count += 1
#                     if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
#                         right_shift_count += 1

#             return max(left_shift_count, right_shift_count)

#         max_overlaps = 0
#         # move one of the matrice up and left and vice versa.
#         # (equivalent to move the other matrix down and right)
#         for y_shift in range(0, dim):
#             for x_shift in range(0, dim):
#                 # move the matrix A to the up-right and up-left directions
#                 max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
#                 # move the matrix B to the up-right and up-left directions
#                 #  which is equivalent to moving A to the down-right and down-left directions 
#                 max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

#         return max_overlaps