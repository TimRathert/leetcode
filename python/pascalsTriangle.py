def triangle(numRows):
    if numRows == 1:
        return [[1]]
    output =[[1],[1,1]]
    while len(output)<numRows:
        def addRow():
            row = len(output)
            newRow = []
            #print(output[row-1][0+(row-(row-len(newRow)))] + output[row-1][1+(row-(row-len(newRow)))])
            while len(newRow) < row-1:
                newRow.append(
                    (output[row-1][0+(row-(row-len(newRow)))] + output[row-1][1+(row-(row-len(newRow)))])
                )
            newRow.append(1)
            newRow.insert(0,1)        
            output.append(newRow)
        addRow()
    return output
print(triangle(1))