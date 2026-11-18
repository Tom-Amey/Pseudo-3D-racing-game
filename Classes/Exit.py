import pygame

class Exit():
    def exit_error():
        pygame.init()
        time_elapsed_seconds = int(((pygame.time.get_ticks()))/50)
        while time_elapsed_seconds < 150:  #window closes after set time of 150s and game does not proceed
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    time_elapsed_seconds = 200
            screen = pygame.display.set_mode((1450,800)) #creating screen
            #outputting text message to user to notify user of unsupported OS
            font = pygame.font.SysFont(None, 24)
            img1 = font.render('An error Occured :( ', True, (255,255,255))
            img2 = font.render('Please ensure you are using a compatible device', True, (255,255,255))
            screen.blit(img1, (700, 400))
            screen.blit(img2,(700, 600))
            pygame.display.update()

                
    