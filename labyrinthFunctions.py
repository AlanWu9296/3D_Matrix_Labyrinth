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

def identifyBoundarys(logicPoints): #{(x,y,z):LogicPoint} -> {(x,y,z):LogicPoint}
    neighborPoints = []
    for ptKey in logicPoints.keys():
        pt = logicPoints[ptKey]
        neighborCount = 0
        for key in pt.neighbors:
            if pt.neighbors[key] != None:
                neighborCount = neighborCount + 1
        if neighborCount != 6:
            pt.isBoundary = True
            neighborPoints.append(pt)
    return neighborPoints


def makePairs(PointsList): # [pt] -> [(pt,pt)]
    i = 0
    n = len(PointsList)
    PairList = []
    if n >= 2:
        while i < (n-1):
            PairList.append((PointsList[i],PointsList[i+1]))
            i = i+1
    return PairList

"""
These are all methods to make the routes which must conform to the protocal:{(x,y,z):LogicPoint} -> [(pt...)]
"""
def binaryTree(logicPoints):
    # type: (object) -> object
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

def recursiveAddition(logicPoints, neighborPoints):
    # type: (object) -> object
    n = rs.GetInteger("Please indicate how many times the addition will do",10)
    finalPath = []
    path = []
    count = 0
    keys = logicPoints.keys()

    while count < n and len(neighborPoints) != 0:
            startPt = choice(neighborPoints)
            neighborPoints.remove(startPt)
            path.append(startPt.position)
            startPtNeighborKeys = startPt.neighbors.keys()
            while len(startPtNeighborKeys) != 0:
                nextNeighbor = startPt.neighbors[startPtNeighborKeys.pop()]
                if nextNeighbor != None:
                    path.append(nextNeighbor.position)
                    direction = rs.VectorSubtract(nextNeighbor.position, startPt.position)
                    while nextNeighbor.isBoundary != True:
                        neighborPoints.append(nextNeighbor)
                        nextNeighbor.isBoundary = True
                        nextPtKey = str(rs.VectorAdd(nextNeighbor.position, direction))
                        nextNeighbor = logicPoints[nextPtKey]
                        path.append(nextNeighbor.position)
                    else:
                        linkPairs = makePairs(path)
                        removePair = choice(linkPairs)
                        linkPairs.remove(removePair)
                        finalPath = finalPath + linkPairs
                        path = [startPt.position]

            count = count + 1
            path = []
    return finalPath


"""
These are all the methods to use the generated path to make the graphic presentation which must conform to the protocal:
[[pt...]] -> Rhino 3d shapes
"""
def simpleLine(path):
    # type: (object) -> object
    for points in path:
        rs.AddLine(points[0], points[1])
        pass
    pass
