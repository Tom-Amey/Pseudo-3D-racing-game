import pygame
class img: 
    def __init__(self, x, y,screen, img):      #stock variables including img, position and screen
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.img_loaded = pygame.image.load(img)
    def load_img_asalpha(self): #load image as alpha to convert to numeric value to scale/get_width() functions etc
        img_loaded = pygame.image.load(self.img).convert_alpha()
        return img_loaded
    def flip_img_vertical(self): #flip the image 180 degrees and blit to pygame window
        img_loaded = pygame.image.load(self.img).convert_alpha()
        img_loaded = pygame.transform.flip(img_loaded, True, True)
        self.screen.blit(img_loaded, (self.x, self.y))
    def display(self): #display img
        self.screen.blit(self.img_loaded, (self.x,self.y)) #display image to screen at (x,y)