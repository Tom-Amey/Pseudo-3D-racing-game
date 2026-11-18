import Exit
import pygame
import Button1

#class designed to check the status of prog and return linking displays between menu and levels/starting and loading
class CheckState:
    def __init__(self):
        pass
    def check_sys(self, sys_type, allowed_sys):
        if sys_type in allowed_sys: 
            valid = True #valid OS so game continues to run
        else:
            Exit.Exit.exit_error() #calls exit to stop game from running as user has unsupported OS 
        return valid

    def DisplayMetrics(self, timePlayed, coins, lives, screen):   #used to display stats during any level
        timePlayed = round(timePlayed)
        screen.fill((168,230,29)) #background colour
        title = pygame.image.load("Game_stats.png")
        screen.blit(title, (200, 100)) #display title text
        pygame.draw.polygon(screen, (255,255,255), [(300, 190), ((300),190), (300, 200), ((300),200 )]) #display title underline
        
        #display stats using font and blit
        font = pygame.font.SysFont(None, 50)
        img1 = font.render(("Lives Remaining: "+str(lives)), True, (255, 255, 255))
        img2 = font.render(("Time played: "+str(timePlayed))+"s", True, (255, 255, 255))
        img4 = font.render(("Coins: "+str(coins)), True, (255,255,255))
        img5 = pygame.image.load("HomeButton.png").convert_alpha()
        return_to_menu_button = Button1.Button(750, 500, img5, 0.75) #create home button to return to menus
        return_to_menu_button_pressed = return_to_menu_button.draw(screen)
        screen.blit(img1, (300, 280))
        screen.blit(img2, (300, 380))
        screen.blit(img4, (300, 480))
        return return_to_menu_button_pressed


class DisplayMessage():
    def __init__(self, text, screen):
        self.text = text
        self.screen = screen
    def Create(self, X, Y):
        font = pygame.font.SysFont(None, 50)
        img1 = font.render(self.text, True, (255, 255, 255))
        self.screen.blit(img1,(X, Y))