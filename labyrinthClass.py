import rhinoscriptsyntax as rs

class LogicPoint():
    """
       This is the extension of the rhino Point3d Class in order to conviently store some relevent datas
    """
    def __init__(self,rhinoPoint,layer='LogicPoint', color=(150,0,0)):
        
        """ These attributes are not general and are for specific algorithms to use """
        self.isVisited = False # wait to be changed by PathMaker class
        self.isChosen = False # wait to be changed by PathMaker class
        self.isBoundary = False # wait to be changed by PathMaker class
        
        self.position = rs.PointCoordinates(rhinoPoint)
        self.neighbors = {
        "left" : None,
        "right" : None,
        "up" : None,
        "down" : None,
        "above" : None,
        "below" : None
        }
    
