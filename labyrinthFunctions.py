from random import choice
import rhinoscriptsyntax as rs


def identifyNeighbors(logicPoints): #{(x,y,z):LogicPoint} -> {(x,y,z):LogicPoint}
    unitX = rs.GetReal("the unit distance in x direction", 1)
    unitY = rs.GetReal("the unit distance in y direction", 1)
    unitZ = rs.GetReal("the unit distance in z direction", 1)
    directionCheck = {
    "left" : (-unitX,0,0),
    "right" : (unitX,0,0),
    "up" : (0,unitY,0),
    "down" : (0,-unitY,0),
    "above" : (0,0,unitZ),
    "below" : (0,0,-unitZ)
    }
    for ptKey in logicPoints.keys():
        pt = logicPoints[ptKey]
        for key in directionCheck.keys():
            newPosition  = str(rs.VectorAdd(pt.position, directionCheck[key]))
            x = logicPoints.has_key(newPosition)
            if logicPoints.has_key(newPosition) :
                pt.neighbors[key] = logicPoints[newPosition]
                pass
            pass
        pass
    pass
"""
These are all methods to make the routes which must conform to the protocal:{(x,y,z):LogicPoint} -> [(pt...)]
"""
def binaryTree(logicPoints):
    path = []
    for key in logicPoints.keys():
        logicPoint = logicPoints[key]
        potentialLink = []
        for neighborKey in logicPoint.neighbors.keys():
            if neighborKey == "right" or neighborKey == "above" or neighborKey == "up":
                potentialNeighbor = logicPoint.neighbors[neighborKey]
                if potentialNeighbor != None:
                    potentialLink.append(potentialNeighbor)
                pass
        if len(potentialLink) != 0:
            linkPoint = choice(potentialLink)
            path.append((logicPoint.position,linkPoint.position))
            pass
        pass
    return path
    pass

"""
These are all the methods to use the generated path to make the graphic presentation which must conform to the protocal:
[[pt...]] -> Rhino 3d shapes
"""
def simpleLine(path):
    for points in path:
        rs.AddLine(points[0], points[1])
        pass
    pass
