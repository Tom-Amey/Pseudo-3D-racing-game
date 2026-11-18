import time
import Menu
import PlayerData
import Level1
import PseudoLogic
import LoginPage
import SQLMethods
import dictionaryMethods
import check_sys
import Loading
import pygame
import PseudoManager
# Read this for variable definitions and bounds

class loadGameAssets():
    def __init__(self, screen):
        self.screen = screen #passed into from mainloop the constant pygame window throughout game
        self.menu1 = Menu.Menu(screen=self.screen, img1="button_leaderboard.png", img2="button_garage.png", img3="button_play.png", img4="button_login.png") #create menu object with valid arguments
        self.PlayerInfo = PlayerData.PlayerData() #creating playerData object to store user's lives, username and coins after login
        self.level1 = Level1.Level1(self.screen, 0, 0, self.PlayerInfo)  #creating level1 object ready for gameplay
        self.level2 = Level1.Level1(self.screen, 0, 0, self.PlayerInfo) 
        self.levelCoins = 0
        #creating pseudo objects for level3 and level 4
        self.level3 = PseudoLogic.PsuedoLevelLogic(screen=screen, X_RESOLUTION=1450, Y_RESOLUTION=800, BLOCK_DEPTH=400, colour_dict=self.level1.colour_dict, player= self.PlayerInfo)
        self.level4 = PseudoLogic.PsuedoLevelLogic(screen=screen, X_RESOLUTION=1450, Y_RESOLUTION=800, BLOCK_DEPTH=400, colour_dict=self.level1.colour_dict, player=self.PlayerInfo)
        self.Play = False #play becomes true once level is pressed 
        self.Load = False #allows load sequence to run once (at beginning of game)
        self.main_menu_run = False  #holds true when running main menu
        self.level_menu_run = False #holds true when running 
        self.OutOfLives = False #holds true when playerData retains lives value < 1
        self.Start_time = 0 #records time of 2D level start time (float>=0)
        self.SQLMethods = SQLMethods.DataBaseMethods(self.PlayerInfo)# initialising SQLmethods for logins and coin updates etc
        self.LoginPage = LoginPage.LoginPage(self.SQLMethods) #initialising login page so on pressed functionality can be ran immediately
        self.timePlayed = 0 #stores time played for each level must be float>= 0
        self.dictionaryMethods = dictionaryMethods.dictionaryMethods() #initialising dictionarymethods for use in Pseudo levels
        self.CheckStateObj = check_sys.CheckState() #calls and creates CheckState object for checking OS and 
        self.load_page = Loading.Loading(screen=screen, time_elapsed_seconds = int(((pygame.time.get_ticks())/750))) # create load sequence
        self.PseudoManager = PseudoManager.PseudoLevelManager()