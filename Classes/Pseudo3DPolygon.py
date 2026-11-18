import math
import pygame

class Polygon():
    def __init__(self, X_RESOLUTION, Y_RESOLUTION, ROADWIDTH):
        #world coordinates
        self.x_world = 0 
        self.y_world = 0
        self.z_world = 0
        #screen coordinates and scales
        self.X_screen = 0
        self.Y_screen = 0 
        self.width = 0
        self.scale = 0
        #screen values
        self.X_RESOLUTION = X_RESOLUTION
        self.Y_RESOLUTION = Y_RESOLUTION
        self.ROADWIDTH = ROADWIDTH
        self.Curvature = 0 #corner ability
        
    def ScaleCoordinates(self,camZ, camX, camY):
        self.scale = (1 / -(math.tan(40))) / (self.z_world - camZ) #scale governed by FOV angle over the distance from z_world to CamZ
        self.X_screen = (self.X_RESOLUTION/2) + (self.x_world - camX) * (self.scale) * (self.X_RESOLUTION/2) #calculating X_screen from the x_world and camX position
        self.Y_screen = (self.Y_RESOLUTION/2) - ((self.y_world - camY) * (self.scale) * (self.Y_RESOLUTION/2))  #calculating Y_screen from the y_world and camY position
        self.width = self.scale * (self.Y_RESOLUTION/2) * self.ROADWIDTH  #width of polys
        
    def DrawPolygon(self, screen, colour, x1, x2, w1, w2, y1, y2):
        #draw the polygon to screen with given colour from calculated screen values
        pygame.draw.polygon(screen, colour, [(x1-w1, y1), (x2-w2, y2), (x2+w2, y2), (x1+w1, y1)]) # as all polygons on the screen follow
