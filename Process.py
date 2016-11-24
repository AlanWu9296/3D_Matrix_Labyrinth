import labyrinthClass as lc
import labyrinthFunctions as lf
import rhinoscriptsyntax as rs

points = rs.GetObjects("Please select all the points matrix for labyrinth")
logicPoints = {}

#initialize
for point in points:
    logicPoint = lc.LogicPoint(point)
    logicPoints[str(logicPoint.position)] = logicPoint
#initialize neighbors
lf.identifyNeighbors(logicPoints)
#genrating paths
path = lf.binaryTree(logicPoints)
#Draw the graph
lf.simpleLine(path)
