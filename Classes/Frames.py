import pygame

class frames_load(): 
    
    def frames_load(screen, frame_num):
        if frame_num == 1:
            frame1 = pygame.image.load("pixil-frame-0.png")
            screen.blit(frame1, (0,-100))
                
        if frame_num == 2:
            frame2 = pygame.image.load("pixil-frame-1.png")
            screen.blit(frame2, (0,-100))
                
        if frame_num == 3:
            frame3 = pygame.image.load("pixil-frame-2.png")
            screen.blit(frame3, (0,-100))
                
        if frame_num == 4:
            frame4 = pygame.image.load("pixil-frame-3.png")
            screen.blit(frame4, (0,-100))
                
        if frame_num == 5:
            frame5 = pygame.image.load("pixil-frame-4.png")
            screen.blit(frame5, (0,-100))
                
        if frame_num == 6:
            frame6 = pygame.image.load("pixil-frame-5.png")
            screen.blit(frame6, (0,-100))
                
        if frame_num == 7:
            frame7 = pygame.image.load("pixil-frame-6.png")
            screen.blit(frame7, (0,-100))
                
        if frame_num > 7:   
            frame8 = pygame.image.load("pixil-frame-7.png")
            screen.blit(frame8, (0,-100))


#once time increases frame num increases 
#each frame number contains some letters of turbo 90 until frame 7 when title fully displayed at final frame