import PseudoLogic
import pygame
import time

class PseudoLevelManager:
    def Initiatelevel(self, level, CurrentLevel, screen, GameAssets):
        #Joining variables to sum all the key variables from all instances of pseudo level
        checkpoints = 0
        ExistingZMovement = 0 
        totaltime = 0
        ExistingCoins = 0
        font = pygame.font.SysFont(None, 75)
        
        while checkpoints < 6 and not level.TerminateLevel:
            #running the pseudo level
            level.Run(CurrentLevel, GameAssets.dictionaryMethods, ExistingCoins)
            #increasing summations of level variables
            delta_x = level.delta_x
            ExistingZMovementLevel = level.totalZMovement
            ExistingTimeLevel = level.time_played
            ExistingCoins+= level.coins
            ExistingZMovement += ExistingZMovementLevel
            totaltime += ExistingTimeLevel
            # if home button pressed or lives are 0 then end loop of level creation and return to main
            if level.TerminateLevel:
                checkpoints = 5
            #creating new instance of pseudo level
            level = PseudoLogic.PsuedoLevelLogic(screen=screen, X_RESOLUTION=1450, Y_RESOLUTION=800, BLOCK_DEPTH=400, colour_dict=GameAssets.level1.colour_dict, player= GameAssets.PlayerInfo)
            #transferring old pseudo level variables to new pseudo level object
            level.delta_x = delta_x
            level.ExistingZMovement += ExistingZMovement
            level.time_played += totaltime
            checkpoints += 1 
            #printing checkpoints to screen and loading new terrain section
            start_time = time.time()
            
            while (time.time() - start_time) < 3:
                CheckpointTxt = font.render(("CHECKPOINT  " + str(checkpoints) + "/5"), True, (255, 255, 255))
                screen.blit(CheckpointTxt, (500, 50))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
        #appending this to main loop so it can access local store of level stats            
        GameAssets.timePlayed = totaltime
        GameAssets.levelCoins = ExistingCoins