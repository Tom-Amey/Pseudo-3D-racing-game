
import random
import pygame
import display_img
import twoD_road_generation
import collisionDetection


class Level1():
    def __init__(self, screen, delta_y, delta_x, player):
            #colours with their respective binary code
        self.colour_dict = {"Black":(0,0,0),
                            "Red": (255,0,0),
                            "light_green": (144,238,144),
                            "dark_green":(0, 154, 0),
                            "green_used": (168,230,29),
                            "grey_used": (180,180,180),
                            "dark_grey_used":(70,70,70),
                            "white_used": (255,255,255)}
        self.delta_y = delta_y #change in y position of player
        self.totalYMovement = 0 #cumalative change in y position
        self.delta_x = delta_x # change in x position of player
        self.screen = screen #pygame window
        # tree image objects
        self.tree1 = display_img.img(50 , -356, self.screen, "tree1.png")
        self.tree2 = display_img.img(50, 100, self.screen, "tree2.png")
        self.tree3 = display_img.img(50, 556, self.screen, "tree3.png")
        self.tree4 = display_img.img(1150, -356, self.screen, "tree1.png")
        self.tree5 = display_img.img(1150, 100, self.screen, "tree3.png")
        self.tree6 = display_img.img(1150, 556, self.screen, "tree2.png")
        #y coordinates for road markings
        self.y0 = 0
        self.y1 = 115
        self.y2 = 230
        self.y3 = 345 
        self.y4 = 460
        self.y5 = 575
        self.y6 = 690
        self.y7 = 805
        self.y8 = -75
        self.lane_of_bot = 400 #x position of bot
        self.bot1_y = -620 #starting y psoition of bot
        self.lane_of_bot = 400
        self.first_turn = True #player's delta_x changed once
        self.bot_type = "car1.png" #bot img
        #load player car img
        self.player_car = pygame.image.load("car7.png")
        self.player_car = pygame.transform.rotate(self.player_car, 180)
        self.player_x = 650 # player x start position
        self.player = player #loading PlayerData into level
        self.coins = 0 #coins during level
        
    def level1_bot_control(self):
        if self.bot1_y ==-620 or self.bot1_y >928: #if bot off screen or just starting out in road reset bot values
            self.lane_of_bot = random.choice([400,685,945])
            self.bot1_y = -(random.randrange(300, 900))
            self.bot_type = random.choice(["car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png", "car7.png"])
        self.bot1_y = self.bot1_y + self.delta_y + 4 #increase boy y position linearly as well as adding delta_y to delta y
        bot = display_img.img(self.lane_of_bot, self.bot1_y, self.screen, self.bot_type) #display bot to screen
        if self.bot_type == "car1.png" or self.bot_type == "car3.png" or self.bot_type == "car4.png" or self.bot_type == "car5.png" or self.bot_type == "car6.png":
            bot.flip_img_vertical() #if these cars are the bot then it must be flipped then displayed
        else:
            bot.display()
        
    
    def lv1_lvl2_terrain(self):
        self.screen.fill(self.colour_dict["green_used"]) #setting background colour 
        pygame.draw.rect(self.screen, self.colour_dict["grey_used"], (350,0,750,1500)) #drawing road base
        self.tree1.y += self.delta_y # increasing the y coordinates of all trees as change in playerY position.
        self.tree2.y += self.delta_y
        self.tree3.y += self.delta_y
        self.tree4.y += self.delta_y
        self.tree5.y += self.delta_y
        self.tree6.y += self.delta_y
        self.y0 += self.delta_y # increasing the y coordinates of all the road markings as change in playerY position
        self.y1 += self.delta_y
        self.y2 += self.delta_y
        self.y3 += self.delta_y
        self.y4 += self.delta_y
        self.y5 += self.delta_y
        self.y6 += self.delta_y
        self.y7 += self.delta_y
        # two lots of road created for a 3 lane road.
        lines1 = twoD_road_generation.draw_vertical_2d_road(self.screen, 590, self.y0, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7,self.y8, self.colour_dict)
        lines2 = twoD_road_generation.draw_vertical_2d_road(self.screen,840, self.y0, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7,self.y8, self.colour_dict)
        # when first road marking greater than 40 a new road marking is formed at top of screen.
        if self.y0>=40:
            self.y8 += self.delta_y
        #when road reaches original position reset variables
        if lines1 == False and lines2 == False:
            self.y0, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7, self.y8 = 0, 115, 230, 345, 460, 575, 690, 805, -75
        #checking trees for being off the screen so regeneration of trees required
        if self.tree4.y >= 1026 or self.tree1.y >= 1026:
            self.tree4.y = -356
            self.tree1.y = -356
            self.tree4.img = random.choice(["tree1.png", "tree2.png", "tree3.png"]) 
            self.tree1.img = random.choice(["tree1.png", "tree2.png", "tree3.png"]) 
        if self.tree2.y >= 1026 or self.tree5.y >= 1026:
            self.tree2.y = -356
            self.tree5.y = -356
            self.tree2.img = random.choice(["tree1.png", "tree2.png", "tree3.png"]) 
            self.tree5.img = random.choice(["tree1.png", "tree2.png", "tree3.png"])
        if self.tree6.y >= 1026 or self.tree3.y >= 1026:
            self.tree6.y = -356
            self.tree3.y = -356
            self.tree6.img = random.choice(["tree1.png", "tree2.png", "tree3.png"]) 
            self.tree3.img = random.choice(["tree1.png", "tree2.png", "tree3.png"]) 
        #displaying all trees to pygame window
        self.tree1.display(), self.tree2.display(), self.tree3.display(), self.tree4.display(), self.tree5.display(), self.tree6.display() 
        
    def car(self): 
        #increasing total Y movement as delta_y changes of player
        self.totalYMovement += self.delta_y
        # increasing the coins for every y distance travelled
        self.coins = round(self.totalYMovement/ 3000)
        # altering playerX with the change in x due to key presses made by user
        self.player_x += self.delta_x
        if self.delta_x != 0:
            if self.delta_x > 0:
                #display car turning right
                self.player_car = pygame.transform.rotate(pygame.image.load("car7_right.png"), 180)
                self.screen.blit(self.player_car, (self.player_x, 630))
            elif self.delta_x < 0:
                #display car turning left
                self.player_car = pygame.transform.rotate(pygame.image.load("car7_left.png"), 180)
                self.screen.blit(self.player_car, (self.player_x, 630))
    
        else:
            #display straight car image
            self.player_car = pygame.transform.rotate(pygame.image.load("car7.png"), 180)
            self.screen.blit(self.player_car, (self.player_x, 650))
            self.first_turn = True
        #check for collision between bots and player car
        collide = collisionDetection.check_2D_collision(self.player_x, self.lane_of_bot, 650, self.bot1_y)
        if collide == True:
            #reduce lives if collision is true and reproduce a new bot
            self.player.lives = self.player.lives -1
            self.bot1_y = 928
            # display lives to the user in screen
        for i in range(0, self.player.lives):
            self.screen.blit(pygame.image.load("heart.png"), ((i*64), 0))
        