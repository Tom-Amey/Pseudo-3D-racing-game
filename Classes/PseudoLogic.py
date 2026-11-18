import pygame
import time
import sys
import SpriteManager
import random 
from PseudoAssets import LoadPsuedoAssets


pygame.init() # initialise pygame for use
class PsuedoLevelLogic(LoadPsuedoAssets): #inherit and construct all psuedo assets (no global variables)
    def __init__(self, screen, X_RESOLUTION, Y_RESOLUTION, BLOCK_DEPTH, colour_dict, player):
        super().__init__(screen, X_RESOLUTION, Y_RESOLUTION, BLOCK_DEPTH, colour_dict, player,)

    def Run(self, LevelNumber, dictionaryMethods, ExistingCoins):
        zAddition =0
        if LevelNumber == 3:
           zAddition = 25
        start_time = time.time()
        CumalativeCurvature = 0 #stores the total curvature experienced by player (sum of all popped polygons' curvature var)
        deltaCurve = 0  #change in curvature for camera position
        dCurve = 0 #change in curvature for player position
        timeKeyUp = 0 #time key up has been lifted to slow player car down in proprotion to time key has been up
        polygons1 = self.TerrainObjectCreator.create_straight_road(0) #create straight road to start
        bot1 = SpriteManager.BotOnRoad(polygons1) #format bot ready for displaying
        while not self.TerminateLevel and self.totalZMovement<350000:  #at set distance or lives level will terminate

            self.coins = round(self.totalZMovement / 10000)  #track coin gains 
            if timeKeyUp != 0:
                # changing delta_z increase to slowly reduce until speed/delta_z reaches 0
                delta_z_slowing = round(74+zAddition - ((time.time() - timeKeyUp) * 25))
                self.totalZMovement += delta_z_slowing
                self.delta_z += delta_z_slowing 
                if (time.time() - timeKeyUp) * 25 >= 74 + zAddition:
                    timeKeyUp = 0
            
            
            self.screen.fill(self.colour_dict["light_green"])
            deltaCurve = 0
            CumalativeCurvature = 0
            
            # seperate in level key control to avoid lag between mainloop and 3D levels
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or timeKeyUp != 0:
                if keys[pygame.K_UP]:
                    self.delta_z += 75 + zAddition
                    self.totalZMovement += 75 + zAddition
                    self.movementSFX.play()
                if keys[pygame.K_RIGHT]:
                    self.delta_x = self.delta_x + 20 
                    self.player_image_direction = self.player_car_right
                if keys[pygame.K_LEFT]:
                    self.delta_x = self.delta_x - 20
                    self.player_image_direction = self.player_car_left
            if keys[pygame.K_DOWN]:
                self.delta_z -= 0
            self.delta_x = self.delta_x + dCurve

         
            #loop through all polygon objects and draw them
            for i in range (1, len(polygons1)-1):
                if i >= len(polygons1):
                    pass
                else:
                    current_polygon = polygons1[i]
                    CumalativeCurvature += deltaCurve
                    deltaCurve += current_polygon.Curvature
                    current_polygon.ScaleCoordinates(camZ= self.delta_z, camX= self.delta_x - CumalativeCurvature, camY=800)
        

                    if i % 2 == 0:
                        grass_colour = self.colour_dict["light_green"]
                        markings = self.colour_dict["white_used"]
                    else:
                        grass_colour = self.colour_dict["dark_green"]
                        markings = self.colour_dict["dark_grey_used"]
            
                    current_polygon.DrawPolygon(self.screen, grass_colour, 0, 0,self.X_RESOLUTION, self.X_RESOLUTION, (self.y_previous), (current_polygon.Y_screen)) # x1, x2, w1, w2, y1, y2
                    current_polygon.DrawPolygon(self.screen, self.colour_dict["dark_grey_used"], self.x_previous, current_polygon.X_screen,self.w_previous, current_polygon.width, self.y_previous, current_polygon.Y_screen)
                    current_polygon.DrawPolygon(self.screen, markings, self.x_previous, current_polygon.X_screen,self.w_previous*self.road_marking_scale, current_polygon.width *self.road_marking_scale, self.y_previous, current_polygon.Y_screen)
                    
                #Removal of any polygons/objects/sprites off the window/screen 
                if (current_polygon.Y_screen) > self.Y_RESOLUTION+self.BLOCK_DEPTH and len(polygons1)>1: #polys
                    polygons1.pop(i)
                    self.n_pops += 1
                    Temp = {}  #temporary dictionary used for editations
                    if (i + self.n_pops) in self.Sprites: #sprites
                        self.SpritesDeleted += 1
                        BuildTrees = self.Sprites[(i + self.n_pops)].BuildTrees
                        del self.Sprites[(i+self.n_pops)]
                        #now creating a new sprite for every deleted sprite
                        lastKey = dictionaryMethods.getLastKey(self.Sprites)
                        Temp[lastKey+(len(self.Sprites)*5)] = SpriteManager.Sprite(self.TreeType, BuildTrees)
                        Temp.update(self.Sprites)
                        #transfer new correct contents to original sprite list
                        self.Sprites = Temp.copy()
                        Temp.clear()
                    if i == bot1.SegmentNum - self.n_pops: # bots
                        bot1.OnScreen = False

                #store previous values of polygons to draw against
                self.x_previous = current_polygon.X_screen   
                self.y_previous = current_polygon.Y_screen
                self.w_previous = current_polygon.width
                
                #Regeneration of road segment (collection of polygons)
                if self.delta_z > (self.numberOfPolys*self.BLOCK_DEPTH -(self.BLOCK_DEPTH*(self.numberOfPolys/2))) and polygons1[1].Curvature == 0 and polygons1[2].Curvature == 0: 

                    #retain existing objects in dictionary by moving their polygon number to be translated in new regeneration of road
                    ListOfKeys2 = list(self.Sprites.keys())
                    for i in ListOfKeys2:
                        self.Sprites = dictionaryMethods.changeKeyDict(self.Sprites, i, (i-self.n_pops), self.Sprites[i])    
                    
                #setting variables and objects back to default
                    self.SpritesDeleted = 0  
                    polygons1.clear()
                    if LevelNumber == 4:
                        polygons1 = random.choice([self.TerrainObjectCreator.create_straight_road(self.delta_z), self.TerrainObjectCreator.create_left_corner(self.delta_z), self.TerrainObjectCreator.create_right_corner(self.delta_z)]) 
                    elif LevelNumber == 3:
                        polygons1 = self.TerrainObjectCreator.create_straight_road(self.delta_z)
                    self.delta_z = 0
                    
                    #do the same for the bots by getting new polygon number from subtracting number of pops by current polygon number of bot
                    if bot1.OnScreen:
                        bot1.SegmentNum = bot1.SegmentNum - self.n_pops
                    else:
                        bot1 = SpriteManager.BotOnRoad(polygons1)
                        
                    self.total_n_pops += self.n_pops
                    self.n_pops = 0
                     
                #seperate (external from mainloop) event control for any keys that have been released not pressed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            self.player_image_direction = self.player_car_straight
                        if event.key == pygame.K_UP:
                            timeKeyUp = time.time()
                            self.movementSFX.stop()
            
            if polygons1[1].Curvature != 0 and keys[pygame.K_UP]:
                dCurve = -(polygons1[1].Curvature) *1.5
                
            elif polygons1[1].Curvature != 0 and not keys[pygame.K_UP]:
                dCurve = 0
                
            else:
                dCurve = 0
                
                
            #producing sky/background
            self.screen.blit(self.bg, (0,-15))
            self.screen.blit(self.bg, (612,-15))
            self.screen.blit(self.bg, (1224, -15))
            
            
            #sprite management
            for spriteNum in self.Sprites:
                if (spriteNum-self.n_pops)>len(polygons1)-1:# or self.Sprites[spriteNum].CurrentCrash(self.player_image_direction):
                    pass
                else:
                    #scaling valid sprites each frame and displaying to screen
                    if self.Sprites[spriteNum].SideOfRoad == "lhs":
                        self.Sprites[spriteNum].LeftHandImageScale(polygons1[(spriteNum-self.n_pops)], 3000)
                        self.screen.blit(self.Sprites[spriteNum].Img, (self.Sprites[spriteNum].X_screen, self.Sprites[spriteNum].Y_screen))
                    elif self.Sprites[spriteNum].SideOfRoad == "rhs":
                        self.Sprites[spriteNum].RightHandImageScale(polygons1[(spriteNum-self.n_pops)], 3000)
                        self.screen.blit(self.Sprites[spriteNum].Img, (self.Sprites[spriteNum].X_screen, self.Sprites[spriteNum].Y_screen))
                    elif self.Sprites[spriteNum].SideOfRoad == "lhs+rhs":
                        self.Sprites[spriteNum].RightHandImageScale(polygons1[(spriteNum-self.n_pops)], 1500)
                        self.screen.blit(self.Sprites[spriteNum].Img, (self.Sprites[spriteNum].X_screen, self.Sprites[spriteNum].Y_screen))
                        self.Sprites[spriteNum].LeftHandImageScale(polygons1[(spriteNum-self.n_pops)], 1500)
                        self.screen.blit(self.Sprites[spriteNum].Img, (self.Sprites[spriteNum].X_screen, self.Sprites[spriteNum].Y_screen))  

            #bot management               
            if bot1.OnScreen and (bot1.SegmentNum-self.n_pops)> 1:
                if bot1.lane == "rhl":    
                    bot1.RightHandLaneScale((polygons1[bot1.SegmentNum-self.n_pops]))
                    self.screen.blit(bot1.BotImg, (bot1.X_screen, bot1.Y_screen))
                if bot1.lane == "lhl":
                    bot1.LeftHandLaneScale(polygons1[bot1.SegmentNum-self.n_pops])
                    self.screen.blit(bot1.BotImg, (bot1.X_screen, bot1.Y_screen))
                if (bot1.SegmentNum - self.n_pops) == 2:
                    if bot1.CurrentCrash(self.player_image_direction, self.centralPlayerPosition[0]):
                        self.Player.lives -= 1
                    
            # Printing camX, camY, camZ, hearts and coins to GUI using fonts and blits                                   
            CamXWord = self.font1.render("CamX: "+str(self.delta_x), True, (255, 255, 255))
            CamYWord = self.font1.render(("CamY: "+str(0)), True, (255, 255, 255))
            CamZWord = self.font1.render(("CamZ: "+str(round(self.totalZMovement+self.ExistingZMovement))), True, (255,255,255))
            CoinsWord = self.font2.render((str(self.coins+ExistingCoins)), True, (255,255,255))
            HeartsWord = self.font2.render((str(self.Player.lives)), True, (255, 255, 255))
            self.screen.blit(CamXWord, (0, 10))
            self.screen.blit(CamYWord, (0, 40))
            self.screen.blit(CamZWord, (0, 70))
            self.screen.blit(CoinsWord, (665, 20))
            self.screen.blit(HeartsWord, (780, 20))
            self.screen.blit(self.coinImg, (600, 10))
            self.screen.blit(self.heartImg, (710, 5))
            
            #Displaying player's car
            self.screen.blit(self.player_image_direction, self.centralPlayerPosition)    
            
            #recording if home button pressed, on pressed loop level loop ends
            self.TerminateLevel = self.HomeButton.draw(self.screen)
            if self.Player.lives < 1:
                self.TerminateLevel = True
            
            #event control
            pygame.display.update()
            pygame.event.pump() # clearing event queue to minimise time searching for user actions from older user actions    
        self.time_played = time.time() - start_time
        