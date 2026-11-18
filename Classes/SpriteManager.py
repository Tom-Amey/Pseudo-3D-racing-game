import pygame
import random
import collisionDetection #sprites have responsibility/the functionality to check for collisions

class Sprite():
    def __init__(self, tree, BuildTrees):
        self.BuildTrees = BuildTrees 
        if self.BuildTrees: #if BuildTrees boolean true then build 2 trees one other side of road
            self.Img = pygame.image.load(tree)
            self.SideOfRoad = "lhs+rhs"
            
        else:
            self.SideOfRoad = random.choice(["lhs", "rhs"]) #setting side of rode for sprite by string code 
            self.Img = random.choice([pygame.image.load("billboard1.png"),pygame.image.load("billboard2.png"), pygame.image.load("billboard3.png"), pygame.image.load("billboard4.png")])
            #random image for sign
            
        self.ImgCopy = self.Img #original Img copied so it can be scaled from original and not scaling already scaled images which causes pixelation
        self.X_screen = 0 
        self.Y_screen = 0 
        #screen coordinates for sprite
        self.RandomWidthAdjustment = random.randrange(0, 30) #this adds some distance between road and sprite for more random placement of sprite
        self.OriginalSpriteHeight = self.Img.get_height() 
        self.OriginalSpriteWidth = self.Img.get_width()
        #getting original height and width
        
    #much like 3D polygons' scale coordinate function returns valid scaled image with X and Y screen coordinate    
    def LeftHandImageScale(self, Segment, scale):  
        if Segment.scale < 0:
            pass
        else:
            self.Img = pygame.transform.scale(self.ImgCopy, (int(self.OriginalSpriteWidth * scale * Segment.scale), int(self.OriginalSpriteHeight * scale * Segment.scale))) #scale image using polygon scale and standard arbitary value
        SegmentLeftCornerX = Segment.X_screen - Segment.width
        self.X_screen = SegmentLeftCornerX - int(self.Img.get_width()) - self.RandomWidthAdjustment
        self.Y_screen = (Segment.Y_screen - self.OriginalSpriteHeight) + (self.OriginalSpriteHeight - (self.Img.get_height()))
        #calculate X and Y screen from differences between road polygon and sprite

    def RightHandImageScale(self, Segment, scale): #scaling Img same for both left and right hand side but X and Y screen calculation changes
        if Segment.scale < 0:
            pass
        else:
            self.Img = pygame.transform.scale(self.ImgCopy, (int(self.OriginalSpriteWidth * scale * Segment.scale), int(self.OriginalSpriteHeight * scale * Segment.scale)))
        SegmentRightCornerX = Segment.X_screen+Segment.width
        self.X_screen = SegmentRightCornerX + int(self.Img.get_width()) + self.RandomWidthAdjustment
        self.Y_screen = (Segment.Y_screen - self.OriginalSpriteHeight) + (self.OriginalSpriteHeight - (self.Img.get_height()))

    def CurrentCrash(self, playerRect): #returns a boolean value calculated by the CollisionDetection object
        return collisionDetection.check_3D_collision(playerRect, self.Img)
         
         
         
class BotOnRoad():
    def __init__(self, polygons):
        self.OnScreen = True  #holds true whilst bot if not off the screen
        self.SegmentNum = random.randrange(20, len(polygons)-35)   #choose random position/polyonNum for bot to be placed on
        self.Segment = polygons[self.SegmentNum]  #finding respective polygon in polygon list so its variables like sacale can be accessed
        self.lane = random.choice(["lhl", "rhl"])  #decide lane by string code
        self.Bot = random.choice(["bot1.png", "bot2.png", "bot3.png", "bot4.png"])   #load bot img
        self.BotImg = pygame.image.load(self.Bot)
        self.BotImgCopy = self.BotImg
        self.X_screen = 0 
        self.Y_screen = 0 
        self.OriginalBotHeight = self.BotImg.get_height() 
        self.OriginalBotWidth = self.BotImg.get_width()
        
    def LeftHandLaneScale(self, Segment):
        if Segment.scale < 0:
            pass
        else:
            self.BotImg = pygame.transform.scale(self.BotImgCopy, (int(self.OriginalBotWidth * 4000 * Segment.scale), int(self.OriginalBotHeight * 4000 * Segment.scale)))
        self.X_screen = Segment.X_screen - 0.5 * Segment.width
        self.Y_screen = self.Y_screen = (Segment.Y_screen - self.BotImg.get_height())
        
    def RightHandLaneScale(self, Segment):
        if Segment.scale < 0:
            pass
        else:
            #calculate scale and the X and Y screen coordinates 
            self.BotImg = pygame.transform.scale(self.BotImgCopy, (int(self.OriginalBotWidth * 4000 * Segment.scale), int(self.OriginalBotHeight * 4000 * Segment.scale)))
        self.X_screen = Segment.X_screen
        self.Y_screen = (Segment.Y_screen - self.BotImg.get_height()) 
    
    def CurrentCrash(self, Player, PlayerX): #returns boolean for collisionDetection object
        self.OnScreen = False
        return collisionDetection.check_3D_collision(Player, self.BotImg, PlayerX, self.X_screen)