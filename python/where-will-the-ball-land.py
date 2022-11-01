from jinja2 import Undefined


def findBall(grid):
    class Ball:
        def __init__(self, startPos, neighbors, endPos):
            self.startPos = startPos
            self.neighbors = {}
            self.endPos = Undefined
    


print(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))