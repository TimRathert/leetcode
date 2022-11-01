from jinja2 import Undefined


def findBall(grid):
    output = []
    def eachBall(startIndex):
        class Ball:
            def __init__(self, startPos):
                self.startPos = startPos
                self.currentPos = startPos
                self.endPos = None

        newBall = Ball(startIndex)        
        row = 0
        var = None
        while newBall.endPos == None:
            try:
                var = grid[row][newBall.currentPos] + grid[row][(newBall.currentPos) + grid[row][newBall.currentPos]]
            except IndexError:
                newBall.endPos = -1
                if len(output) < len(grid[0]):
                    output.append(newBall.endPos)
            else:
                if var == 0:
                    newBall.endPos = -1
                    if len(output) < len(grid[0]):
                        output.append(newBall.endPos)
                else:
                    newBall.currentPos += grid[row][newBall.currentPos] 
                    row += 1
            if row == len(grid)-1:
                newBall.currentPos += grid[row][newBall.currentPos] 
                newBall.endPos = newBall.currentPos
                if len(output) < len(grid[0]):
                    output.append(newBall.endPos)
                break
                # print(newBall.startPos, newBall.currentPos)

    for i in range(len(grid[0])):
        eachBall(i)

    return output

    


# print(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
# print(findBall([[-1]]))
# print(findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
# print(findBall([[1]]))
print(findBall([[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]))