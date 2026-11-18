import Pseudo3DPolygon
import random

class PsuedoRoadCreator():
    # creating variables used in formating the road segments/collection of polygon
    def __init__(self, BLOCK_DEPTH):
        self.NumberOfPolys = 75
        self.BlOCK_DEPTH = BLOCK_DEPTH
        self.NatureOfTerrain = random.choice(["straight", "leftcorner", "rightcorner"])
        self.CurveGradient = random.choice([2, 4, 6, 8, 10, 15, 20])

         
    def create_straight_road(self, camZ):
        polygons = []
        for i in range(1, self.NumberOfPolys):
            polygon = Pseudo3DPolygon.Polygon(X_RESOLUTION=1450, Y_RESOLUTION=800, ROADWIDTH=1500) # first form the polygon objects
            polygon.z_world= ((i*self.BlOCK_DEPTH)+0.000001) #alter the z_world coordiante for each polygon to make a straight road
            polygon.ScaleCoordinates(camZ= camZ, camX=400, camY=800) #scale the coordinates with their respective world coordinates mapped to screeen coordinates
            polygons.append(polygon) # listing all segment objects
        return polygons
    
    def create_left_corner(self, camZ):
        polygons = []
        for i in range(1, self.NumberOfPolys):
            polygon = Pseudo3DPolygon.Polygon(X_RESOLUTION=1450, Y_RESOLUTION=800, ROADWIDTH=1500)
            polygon.z_world= ((i*self.BlOCK_DEPTH)+0.000001) 
            polygon.ScaleCoordinates(camZ= camZ, camX=400, camY=800)
            polygons.append(polygon) #now formed collection of polygons as straight road
        #creating curvature on selected polygons by negation so left corner
        for i in range(1, 20):
            polygons[i].Curvature = 0
        for i in range(20, 40):
            polygons[i].Curvature = -self.CurveGradient
        for i in range(40, self.NumberOfPolys-1):
            polygons[i].Curvature = 0
        return polygons
    
    
    def create_right_corner(self, camZ):
        polygons = []
        for i in range(1, self.NumberOfPolys):
            polygon = Pseudo3DPolygon.Polygon(X_RESOLUTION=1450, Y_RESOLUTION=800, ROADWIDTH=1500)
            polygon.z_world= ((i*self.BlOCK_DEPTH)+0.000001) 
            polygon.ScaleCoordinates(camZ= camZ, camX=400, camY=800)
            polygons.append(polygon) # straight road segment formed
        #creating curvature on selected polygons by addition so right corner 
        for i in range(1, 20):
            polygons[i].Curvature = 0
        for i in range(20, 40):
            polygons[i].Curvature = self.CurveGradient
        for i in range(40, self.NumberOfPolys-1):
            polygons[i].Curvature = 0
        return polygons