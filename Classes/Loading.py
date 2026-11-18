#imports
import pygame
import Button1
import display_img
import Frames
import twoD_road_generation
#import relevant GUI processes to produce the loading screen

class Loading():
    def __init__(self, screen, time_elapsed_seconds):
        
        #colours for displaying shapes
        self.colour_dict = {"Black":(0,0,0),
                            "Red": (255,0,0),
                            "green_used": (168,230,29),
                            "grey_used": (180,180,180),
                            "dark_grey_used":(70,70,70),
                            "white_used": (255,255,255)}
        #variables for road movement
        self.x_coordinate_dict = {"road_x0":-60,
                                    "road_x1":140,
                                    "road_x2":340,
                                    "road_x3":540,
                                    "road_x4":740,
                                    "road_x5":940,
                                    "road_x6":1140,
                                    "road_x7":1340,
                                    "road_x8":1440}

        self.cumalative_var = 0  #stores the cumalative movement in road markings
        self.start_pressed = False #store boolean value for button
        self.load_menu = False #returns this ready to load main menu when start pressed
        self.start_img = pygame.image.load('start_button.png').convert_alpha() #load start button Img
        self.start_button = Button1.Button(400, 450, self.start_img, 6) #initialise Button object for start button
        self.car_x = 1 # stores x position of displayed car on load screen
        self.clock = pygame.time.Clock() #controls time in loop
        self.screen = screen  #transfers main pygame window to main.
        self.time_elapsed_seconds = time_elapsed_seconds

                
    def load_page(self):
        Frames.frames_load.frames_load(self.screen, self.time_elapsed_seconds) #loads frame to output Turbo 90 title
        self.x_coordinate_dict["road_x0"],self.x_coordinate_dict["road_x1"],self.x_coordinate_dict["road_x2"],self.x_coordinate_dict["road_x3"],self.x_coordinate_dict["road_x4"],self.x_coordinate_dict["road_x5"],self.x_coordinate_dict["road_x6"],self.x_coordinate_dict["road_x7"] = (self.x_coordinate_dict["road_x0"] - 10), (self.x_coordinate_dict["road_x1"] - 10),(self.x_coordinate_dict["road_x2"] - 10), (self.x_coordinate_dict["road_x3"] - 10), (self.x_coordinate_dict["road_x4"] - 10), (self.x_coordinate_dict["road_x5"] - 10), (self.x_coordinate_dict["road_x6"] - 10), (self.x_coordinate_dict["road_x7"] - 10)     
        #decreasing each x coordinate of road markings to simulate movement
        road_creation = twoD_road_generation.draw_horizontal_road(self.screen, self.x_coordinate_dict["road_x0"],self.x_coordinate_dict["road_x1"],self.x_coordinate_dict["road_x2"],self.x_coordinate_dict["road_x3"],self.x_coordinate_dict["road_x4"],self.x_coordinate_dict["road_x5"],self.x_coordinate_dict["road_x6"],self.x_coordinate_dict["road_x7"],self.x_coordinate_dict["road_x8"],self.cumalative_var, self.colour_dict)
        # creating the road via the twoD_road_generation class
        if self.cumalative_var >= 100:
            self.x_coordinate_dict["road_x8"] = self.x_coordinate_dict["road_x8"] - 10
        if road_creation == False:
            #setting road markings back to origianl position after cumaltive_var indicates one cycle has completed
            self.x_coordinate_dict["road_x0"], self.x_coordinate_dict["road_x1"], self.x_coordinate_dict["road_x2"], self.x_coordinate_dict["road_x3"], self.x_coordinate_dict["road_x4"], self.x_coordinate_dict["road_x5"],self.x_coordinate_dict["road_x6"], self.x_coordinate_dict["road_x7"], self.x_coordinate_dict["road_x8"], self.cumalative_var= -60, 140, 340, 540, 740, 940, 1140, 1340, 1440, 0            
        if self.start_pressed != True:
            self.start_pressed = self.start_button.draw(self.screen)
            #draw button when not pressed
            
        if self.start_pressed == True:
            #display car and move it along road when start pressed
            self.car_x += (self.car_x ** 0.4)
            ferrari_img = "ferrari.png"
            ferrari_img_class = display_img.img(self.car_x, 300, self.screen, ferrari_img)
            ferrari_img_class.display()    
                
    
            
        if self.car_x>1600:
            self.load_menu = True
            #once car is off the screen the main menu sequence begins
                        
        return self.load_menu
    
    
    
