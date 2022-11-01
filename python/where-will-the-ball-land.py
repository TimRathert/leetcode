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
        #print('started at ', newBall.startPos)
        while newBall.endPos == None:
            try:
                y = ((newBall.currentPos) + grid[row][newBall.currentPos]) if newBall.startPos > 0 else 1
                var = grid[row][newBall.currentPos] + grid[row][y]
            except IndexError:
                newBall.endPos = -1
                
                
            else:
                #if var == 0:
                    #newBall.endPos = -1
                    #output.append(newBall.endPos)
                    #nothing
                if var != 0:
                    newBall.currentPos += grid[row][newBall.currentPos] 
            finally:                
                row += 1
                if newBall.endPos:
                    output.append(newBall.endPos)
                elif var == 0:
                    newBall.endPos = -1
                    output.append(newBall.endPos)
                    break
                elif row == len(grid):
                    if newBall.endPos == None:
                        newBall.endPos = newBall.currentPos
                    output.append(newBall.endPos)
                    #print(newBall.startPos)
                    break


    for i in range(len(grid[0])):
        eachBall(i)

    return output

    

#print(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
#print(findBall([[-1]]))
print(findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
#print(findBall([[1]]))
#print(findBall([[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]))
print(findBall([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]))





# def findBall(grid):
#     output = []
#     def eachBall(startIndex):
#         class Ball:
#             def __init__(self, startPos):
#                 self.startPos = startPos
#                 self.currentPos = startPos
#                 self.endPos = None

#         newBall = Ball(startIndex)        
#         row = 0
#         var = None
#         #print('started at ', newBall.startPos)
#         while newBall.endPos == None:
#             try:
#                 y = (newBall.currentPos) + grid[row][newBall.currentPos] if newBall.startPos > 0 or newBall.startPos < len(grid[0])-1 else 1
#                 var = grid[row][newBall.currentPos] + grid[row][y]
#                 #print(var)
#             except IndexError:
#                 newBall.endPos = -1
#                 if len(output) < len(grid[0]):
#                     output.append(newBall.endPos)
#                     print('started at ', newBall.startPos, 'ended at ', newBall.endPos)
#             else:
#                 if var == 0:
#                     newBall.endPos = -1
#                     if len(output) < len(grid[0]):
#                         output.append(newBall.endPos)
#                 else:
#                     newBall.currentPos += grid[row][newBall.currentPos] 
#                     row += 1
#             if row == len(grid)-1:
#                 newBall.currentPos += grid[row][newBall.currentPos] 
#                 newBall.endPos = newBall.currentPos
#                 if len(output) < len(grid[0]):
#                     output.append(newBall.endPos)
#                     #print('started at ', newBall.startPos, 'ended at ', newBall.endPos)
#                 break
#                 # print(newBall.startPos, newBall.currentPos)

#     for i in range(len(grid[0])):
#         eachBall(i)

#     return output

    


# #print(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
# #print(findBall([[-1]]))
# #print(findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
# #print(findBall([[1]]))
# print(findBall([[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]))