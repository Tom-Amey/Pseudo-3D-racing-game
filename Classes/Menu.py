import Button1
import pygame

class Menu():
    def __init__(self, screen, img1, img2, img3, img4):
        self.background_img = "background.png"  
        self.screen = screen
        #button images stored
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4
        self.font = pygame.font.SysFont(None, 30) #font initialised
        self.coinImg = pygame.image.load("coin.png") #image loaded for menu

    def create_buttons(self, Player):
        
        #load and scaling bg image to fully fit pygame window
        background_load = pygame.image.load(self.background_img)
        background_load = pygame.transform.scale(background_load, (1450,800))
        self.screen.blit(background_load, (0,0))
        
        #creating buttons and displaying them to screen
        button_1a = pygame.image.load(self.img1).convert_alpha()
        Button_1 = Button1.Button(850, 0, button_1a, 0.75) 
        Button_1_pressed = Button_1.draw(self.screen)
        button_2a = pygame.image.load(self.img2).convert_alpha()
        Button_2 = Button1.Button(850, 375, button_2a, 0.75)
        Button_2_pressed = Button_2.draw(self.screen)
        button_3a = pygame.image.load(self.img3).convert_alpha()
        Button_3 = Button1.Button(250, 0, button_3a, 0.75)
        Button_3_pressed = Button_3.draw(self.screen)
        button_4a = pygame.image.load(self.img4).convert_alpha()
        Button_4 = Button1.Button(250, 375, button_4a, 0.75)
        Button_4_pressed = Button_4.draw(self.screen)
        
        Username = self.font.render("Welcome: "+str(Player.Username), True, (255, 255, 255)) #blitting username to screen
        self.screen.blit(Username, (650, 20))
        Coins = self.font.render(": "+str(Player.coins), True, (255, 255, 255))
        self.screen.blit(Coins, (600, 20)) #blitting Player coins to the screen 
        self.screen.blit(self.coinImg, (550, 0))
        return Button_1_pressed, Button_2_pressed, Button_3_pressed, Button_4_pressed
        #returns list of true and false values of which buttons have been pressed
