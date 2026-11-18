import math


def check_2D_collision(x1, x2, y1, y2):
    displacement_between_objects = math.sqrt((math.pow(x1-x2, 2)) + math.pow((y1 - y2), 2)) # using pythagoras 
    if displacement_between_objects < 80: 
        
        collision = True
    else:
        collision = False
    return collision

def check_3D_collision(Player, Bot, PlayerX, BotX):
    PlayerW = Player.get_width()
    BotW = Bot.get_width() 
    if (math.fabs((PlayerX-BotX))+15) < BotW:   #comparing if bot are car are in same width part of screen
        return True
    elif PlayerX > BotX:
        leftHandDistance = abs(PlayerX - (BotX + BotW))  #left hand side of player distance between bot
        if leftHandDistance < 3:
            return True
            
    elif PlayerX < BotX:
        rightHandDistance = math.fabs(BotX - (PlayerX+PlayerW)) #right hand side of player distance between bot
        if rightHandDistance < 3: 
            return True
            #value 3 to avoid image differences and some variance in collisions
  
    else:
        return False
    
    