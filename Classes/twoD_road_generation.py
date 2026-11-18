import pygame

#2-Lane horizontal 2d road

def draw_horizontal_road(screen, x0, x1, x2, x3, x4, x5, x6, x7, x8, cumalative_var, colour_dict):
    repeat = True #when repeat is true the road markings have not reached starting position 
    
    #drawing collection of rects for both road base, road edges and road markings
    pygame.draw.rect(screen, colour_dict["grey_used"], (0,350,1450,350)) # where the second set of parantheses are (x,y,width,height)
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (0,340,7000,10))
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (0,690,7000,10))
    pygame.draw.rect(screen, colour_dict["grey_used"], (0,350,1450,350)) 
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (0,340,7000,10))
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (0,690,7000,10))
    pygame.draw.rect(screen, colour_dict["white_used"],(x0,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x6,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x7,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x5,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x4,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x3,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x2,490,110,41))
    pygame.draw.rect(screen, colour_dict["white_used"],(x1,490,110,41))
    
    #if total movement of road markings reaches value blit additional road marking
    if cumalative_var >= 100:
        pygame.draw.rect(screen, colour_dict["white_used"], (x8,490, 110, 41)) 
    #once road markings moved 200, they have returned to start position 
    if cumalative_var >= 200:
        repeat = False

    return repeat



#2-Lane vertical 2d road

def draw_vertical_2d_road(screen,x_postion, y0, y1, y2, y3, y4, y5, y6, y7, y8, colour_dict):
    repeat = True #when repeat is true the road markings have not reached starting position
    
    #drawing collection of rects for both road base, road edges and road markings
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (340,0,10,1500))
    pygame.draw.rect(screen, colour_dict["dark_grey_used"], (1100,0,10,1500))  
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y0,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y1,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y2,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y3,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y4,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y5,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y6,15,75))
    pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y7,15,75))
    #if y position of bottom road makring reaches value/off screen blit additional road marking
    if  y0>= 75:
        pygame.draw.rect(screen, colour_dict["white_used"],(x_postion,y8,15,75))
    #once new road marking reaches screen the start position of all road markings has been reached and can be regenerated
    if y8 >= 0:
        repeat = False

    return repeat