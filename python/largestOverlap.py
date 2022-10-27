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