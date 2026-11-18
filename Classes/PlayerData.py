class PlayerData():
    #stores relevant data in constructor 
    def __init__(self):
        self.lives = 3
        self.coins = 0 
        self.Username = ""
    def GetData(self, Username, Coins):  #update PlayerData variables once login complete
        self.coins = Coins
        self.Username = Username
