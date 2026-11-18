
import sys, time
import pygame
import GameAssets
import Button_filter
import PseudoLogic
import LoginPage
import Level1
import check_sys
#imports required that cannot be declared in GameAssets


def MainLoop():
    pygame.init() # initialises the pygame and pygame resources

    #Graphics - title and logo
    pygame.display.set_caption("Turbo 90")
    pygame.display.set_icon(pygame.image.load('logo_transparent.png'))
    screen = pygame.display.set_mode((1450,800))#constant screen throughout program
    screen.fill((168,230,29))
    clock = pygame.time.Clock() #set clock
    
    #setting game pathway selection variables to initial boolean values
    Play = False
    Load = False
    main_menu_run = False
    level_menu_run = False
    DisplayStats = False
    
    #2D delta coordiantes
    delta_y = 0
    delta_x = 0
    
    CurrentLevel = 0 #level number: 1,2,3,4 (int[1,2,3,4])
    MainloopAssets = GameAssets.loadGameAssets(screen) #calling load of game assets ready for use
    
    #check OS is valid and contnue game if so
    GameLoop = MainloopAssets.CheckStateObj.check_sys(sys_type=sys.platform, allowed_sys=["linux", "linux2", "win32", "cygwin", "msys", "darwin"])

    while GameLoop:
            clock.tick(45)  #one frame is complete every 0.022s 
            if Play: #handles levels of game
                if MainloopAssets.PlayerInfo.lives<1 or MainloopAssets.level1.totalYMovement >20000 or DisplayStats:  #terminates level if met
                    MainloopAssets.PlayerInfo.coins += MainloopAssets.level1.coins
                    main_menu_run = MainloopAssets.CheckStateObj.DisplayMetrics(timePlayed=MainloopAssets.timePlayed, coins= MainloopAssets.levelCoins, lives =MainloopAssets.PlayerInfo.lives, screen=screen)
                    #resetting values to continue back to MAIN menu
                    MainloopAssets.menu1.img1="button_leaderboard.png" 
                    MainloopAssets.menu1.img2="button_garage.png"
                    MainloopAssets.menu1.img3="button_play.png"
                    MainloopAssets.menu1.img4="button_login.png"
                    if CurrentLevel == 1 or CurrentLevel == 2:
                        MainloopAssets.level1.coins = 0
                        MainloopAssets.level2.coins =0
                    if main_menu_run:
                        DisplayStats = False 
                        Play = False
                        level_menu_run =  False
                        MainloopAssets.PlayerInfo.lives = 3 
                        MainloopAssets.timePlayed = 0
                        MainloopAssets.Start_time = 0 
                        MainloopAssets.levelCoins = 0
                        #creating new level object so that the level just ended can be replayed after returning to menu
                        if CurrentLevel == 1:
                            MainloopAssets.level1 = Level1.Level1(MainloopAssets.screen, 0, 0, MainloopAssets.PlayerInfo)
                        elif CurrentLevel == 2:
                            MainloopAssets.level2 = Level1.Level1(MainloopAssets.screen, 0, 0, MainloopAssets.PlayerInfo)
                #calls in game level functions is not terminating level
                else:
                    if CurrentLevel == 4:
                        MainloopAssets.PseudoManager.Initiatelevel(MainloopAssets.level4, CurrentLevel, screen, MainloopAssets)
                        #once run loop finished return to main to end level and proceed back to menu
                        DisplayStats = True
                        main_menu_run = True
                        MainloopAssets.PlayerInfo.coins += int(MainloopAssets.level4.coins)
                        MainloopAssets.level4 = PseudoLogic.PsuedoLevelLogic(screen=screen, X_RESOLUTION=1450, Y_RESOLUTION=800, BLOCK_DEPTH=400, colour_dict=MainloopAssets.level1.colour_dict, player= MainloopAssets.PlayerInfo)
                        MainloopAssets.menu1.img1="button_leaderboard.png" 
                        MainloopAssets.menu1.img2="button_garage.png"
                        MainloopAssets.menu1.img3="button_play.png"
                        MainloopAssets.menu1.img4="button_login.png"  #update menu button images back to type of game not levels
                        
                    elif CurrentLevel == 3: #same process as level 4 
                        MainloopAssets.PseudoManager.Initiatelevel(MainloopAssets.level3, CurrentLevel, screen, MainloopAssets)
                        #return values to original state and create new level class so it can be replayed
                        DisplayStats = True
                        main_menu_run = True
                        MainloopAssets.PlayerInfo.coins += int(MainloopAssets.levelCoins)
                        MainloopAssets.level3 = PseudoLogic.PsuedoLevelLogic(screen=screen, X_RESOLUTION=1450, Y_RESOLUTION=800, BLOCK_DEPTH=400, colour_dict=MainloopAssets.level1.colour_dict, player= MainloopAssets.PlayerInfo)
                        MainloopAssets.menu1.img1="button_leaderboard.png" 
                        MainloopAssets.menu1.img2="button_garage.png"
                        MainloopAssets.menu1.img3="button_play.png"
                        MainloopAssets.menu1.img4="button_login.png"
                    elif CurrentLevel == 2:
                        #remains in mainloop while 2D levels are completed
                        MainloopAssets.timePlayed = time.time() - MainloopAssets.Start_time
                        MainloopAssets.level2.lv1_lvl2_terrain()
                        MainloopAssets.level2.car()
                        #calls multiple bots to create multiple unlike level1 
                        MainloopAssets.level2.level1_bot_control()
                        MainloopAssets.level2.level1_bot_control()
                        MainloopAssets.level2.level1_bot_control()
                        MainloopAssets.levelCoins = MainloopAssets.level2.coins
                    else:
                        MainloopAssets.timePlayed = time.time() - MainloopAssets.Start_time #updates time played 
                        #calling functions to deal with terrain, bots and player car
                        MainloopAssets.level1.lv1_lvl2_terrain()
                        MainloopAssets.level1.car()
                        MainloopAssets.level1.level1_bot_control()
                        MainloopAssets.levelCoins = MainloopAssets.level1.coins
                        
                     
            else:
                if not Load:
                    MainloopAssets.load_page.time_elapsed_seconds = int(((pygame.time.get_ticks())/750)-4)
                    MainloopAssets.load_page.cumalative_var = MainloopAssets.load_page.cumalative_var + 10
                    Load = MainloopAssets.load_page.load_page()  #once loaded Load is equal to False and never ran again unless restarted
                    if Load == False:
                        main_menu_run = True
                        
                #creating the level menu 
                elif level_menu_run:  
                    level_num = MainloopAssets.menu1.create_buttons(MainloopAssets.PlayerInfo)
                    MainloopAssets.PlayerInfo.lives = 3 
                    
                    #checking the buttons pressed
                    if level_num[0]:  #level 1 
                        Play = True
                        CurrentLevel = 1 
                        MainloopAssets.Start_time = time.time()
                        level_menu_run = False
                    elif level_num[1]:  #level 2
                        Play = True
                        CurrentLevel = 2
                        MainloopAssets.Start_time = time.time()
                        level_menu_run = False
                    elif level_num[2]:  #level 3
                        Play = True
                        CurrentLevel = 3
                        level_menu_run = False
                    elif level_num[3]: #level4
                        Play = True
                        CurrentLevel = 4
                        level_menu_run = False
                        
                        
                elif main_menu_run: #creating the main menu
                    Menu_handling = Button_filter.check_button_menu(button_pressed_list = MainloopAssets.menu1.create_buttons(MainloopAssets.PlayerInfo))
                    
                    #checking the buttons pressed
                    if Menu_handling =="levels":
                        main_menu_run = False
                        level_menu_run = True
                        MainloopAssets.menu1.img1 = "button_lvl1.png"
                        MainloopAssets.menu1.img2 = "button_lvl2.png"
                        MainloopAssets.menu1.img3 = "button_lvl3.png"
                        MainloopAssets.menu1.img4 = "button_lvl4.png"
                        Menu_handling =" "
                        
                        time.sleep(0.2) # allows button pressed list to reset prior to the next loop so the 2nd menu for levels is not affected by the previous button interaction from the main menu
                    elif Menu_handling == "leaderboard":
                        message = check_sys.DisplayMessage("Coming soon!", screen)
                        message.Create(920, 250)
                        time.sleep(0.4)
                        
                    elif Menu_handling == "garage":
                        message = check_sys.DisplayMessage("Coming soon!", screen)
                        message.Create(920, 600)
                        time.sleep(0.4)
                        
                    elif Menu_handling == "login":
                        MainloopAssets.LoginPage.CreateLoginWindow(MainloopAssets.PlayerInfo)
                        MainloopAssets.LoginPage = LoginPage.LoginPage(MainloopAssets.SQLMethods)
                        
                        
        #Event/Keyboard Control for 2D levels only
            for event in pygame.event.get():
                #any gesture to quit
                if event.type == pygame.QUIT:
                    MainloopAssets.SQLMethods.AppendCoins(MainloopAssets.PlayerInfo.coins)
                    GameLoop = False
                #key down from user control
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        delta_y = 10
                    if event.key == pygame.K_LEFT:
                        delta_x = -3
                    if event.key == pygame.K_RIGHT:
                        delta_x = 3
                #key up from user control
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        delta_x = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        delta_y = 0 
                if CurrentLevel ==1:                    
                    MainloopAssets.level1.delta_y = delta_y
                    MainloopAssets.level1.delta_x = delta_x
                if CurrentLevel ==2:
                    MainloopAssets.level2.delta_y = delta_y
                    MainloopAssets.level2.delta_x = delta_x                   
            pygame.display.update() # applying all changes in one instance
        
if __name__ == "__main__":
    MainLoop()  #running main


