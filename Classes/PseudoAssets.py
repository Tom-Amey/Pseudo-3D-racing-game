import pygame
import PseudoRoadCreator
import SpriteManager
import Button1
import random

# read this for Variable Definitions and Bounds for each Variable


class LoadPsuedoAssets:
    def __init__(self, screen, X_RESOLUTION, Y_RESOLUTION, BLOCK_DEPTH, colour_dict, player):
        self.TerminateLevel = False
        self.X_RESOLUTION = X_RESOLUTION # width of screen
        self.Y_RESOLUTION = Y_RESOLUTION #height of screen
        self.BLOCK_DEPTH = BLOCK_DEPTH #any positive integer (natural number)
        self.screen = screen #pygame.set_mode() method 
        self.colour_dict = colour_dict # contains comonly used colours with their binary code
        self.delta_z = 0.000001 #change in players position in Z coordinate
        self.delta_x = 0 #change in players position in Y coordinate
        self.road_marking_scale = 0.05 #size of road markings
        self.x_previous = 0 # previous x coordiante of pseudo3Dpolygon
        self.y_previous = 0 # previous Y coordiante of pseudo3Dpolygon
        self.w_previous = 0 # previous width of pseudo3Dpolygon
        self.time_played = 0 #time when user pressed run
        self.checkpoints = 0
        self.ExistingZMovement = 0 
        self.font1 = pygame.font.SysFont(None, 20) #smaller font for text display
        self.font2 = pygame.font.SysFont(None, 50) #larger font for text display
        self.bg = pygame.image.load("bg_3d.jpg") # 433 pixels high background image (sky)
        self.coinImg = pygame.image.load("coin.png") #coin image
        self.heartImg = pygame.image.load("heart.png") #for lives
        self.player_car_straight = pygame.image.load("player_straight.png").convert_alpha()#image to display when car not turning
        self.player_car_left = pygame.image.load("player_left.png") # image to display when the user is turning left
        self.player_car_right = pygame.image.load("player_right.png") # image to display when the user is turning right
        self.player_car_width = self.player_car_straight.get_width() # width in pixels of player's car
        self.player_car_height = self.player_car_straight.get_height() # height in pixels of player's car
        self.player_car_straight = pygame.transform.scale(self.player_car_straight, (int(self.player_car_width * 1), int(self.player_car_height * 1))) #refreshing car so it is straight
        self.player_image_direction = self.player_car_straight #initial position of player car image
        self.player_car_rect = self.player_car_straight.get_rect() #get rect for scaling and collision mechanisms
        self.centralPlayerPosition = [(self.delta_x-self.player_car_width/2+X_RESOLUTION/2), (Y_RESOLUTION-self.player_car_height)-25] # list of central player position
        self.movementSFX = pygame.mixer.Sound("CarSound.mp3") # initialise car sound
        self.n_pops = 0 #number of removed polygons during one collection of polygons/terrain
        self.polygons1 =  [] #polygons list
        self.totalZMovement = 0 # total distance travelled in Z axis
        self.coins = 0 #users coins
        self.numberOfPolys = 75 #Arbitary value of poylgons to be created
        self.SpritesDeleted = 0 #Number of sprites deleted by the psuedo logic
        self.total_n_pops = 0 #total number of polygons deleted since the start of the level
        self.RoadCreation = PseudoRoadCreator.PsuedoRoadCreator(BLOCK_DEPTH=BLOCK_DEPTH) #initialise road creator class
        self.TempDictionary = {} #for temporarily storing changes to sprite dictionary 
        self.TreeType = random.choice(["tree4.png", "tree5.png"]) #the tree value for current collection of polygons 
        self.Sprites = {137: SpriteManager.Sprite(self.TreeType, True),     #Dictionary of sprites with their PolygonNumber and Sprite Object
           132: SpriteManager.Sprite(self.TreeType, False),
           127: SpriteManager.Sprite(self.TreeType, True),
           122: SpriteManager.Sprite(self.TreeType, False),
           117: SpriteManager.Sprite(self.TreeType, True),
           112: SpriteManager.Sprite(self.TreeType, False),
           107: SpriteManager.Sprite(self.TreeType, True), 
           102: SpriteManager.Sprite(self.TreeType, False),
           97: SpriteManager.Sprite(self.TreeType, True),
           92: SpriteManager.Sprite(self.TreeType, False),
           87: SpriteManager.Sprite(self.TreeType, True),
           82: SpriteManager.Sprite(self.TreeType, False),
           77: SpriteManager.Sprite(self.TreeType, True),
           72: SpriteManager.Sprite(self.TreeType, False),
           67: SpriteManager.Sprite(self.TreeType, True),
           62: SpriteManager.Sprite(self.TreeType, False),
           57: SpriteManager.Sprite(self.TreeType, True),
           52: SpriteManager.Sprite(self.TreeType, False),
           47: SpriteManager.Sprite(self.TreeType, True),
           42: SpriteManager.Sprite(self.TreeType, False),
           37: SpriteManager.Sprite(self.TreeType, True), 
           32: SpriteManager.Sprite(self.TreeType, False),
           27: SpriteManager.Sprite(self.TreeType, True),
           22: SpriteManager.Sprite(self.TreeType, False),
           17: SpriteManager.Sprite(self.TreeType, True),
           12: SpriteManager.Sprite(self.TreeType, False),
           7: SpriteManager.Sprite(self.TreeType, True),
           2: SpriteManager.Sprite(self.TreeType, False)
           }

        self.spritesCopy = self.Sprites.copy() # backup of sprites
        self.TerrainObjectCreator = PseudoRoadCreator.PsuedoRoadCreator(self.BLOCK_DEPTH)# initiating Terrain creator class
        self.HomeButton = Button1.Button(1350, 0, pygame.image.load("homeButton.png"), 0.35) # creating home button ready for level
        self.Player = player # loading the Player's info into var
        