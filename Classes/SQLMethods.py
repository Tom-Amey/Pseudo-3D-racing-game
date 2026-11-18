import sqlite3
from Hashing import Hash


class DataBaseMethods():
    def __init__(self, PlayerInfo):
        self.PlayerUsername = PlayerInfo.Username
        self.PlayerCoins =PlayerInfo.coins  #storing temporary values for user's coins and username
        
        
    def AddNewRecord(self, EnterredUsername, EnterredPassword):
        #database method: adding a new row
        EnterredPassword = Hash.HashText(EnterredPassword)    
        databaseConnection = sqlite3.connect("Turbo90.db")
        cursor = databaseConnection.cursor() # connecting to the database and setting up the curso to execute operations
        insertquery = 'INSERT INTO Users VALUES("'+EnterredUsername+'", "'+EnterredPassword+'", 0);' #storing string query ready to use
        cursor.execute(insertquery) # executing query
        databaseConnection.commit() # follows up command and ensures it is finished to completion
        cursor.close()
        databaseConnection.close() #close database and cursor so they can be used again in later functions
      
    def AppendCoins(self, Coins):
        #database method: updating coins
        databaseConnection = sqlite3.connect("Turbo90.db")
        cursor = databaseConnection.cursor()
        updatequery = 'UPDATE Users SET coins ='+str(Coins)+' WHERE Username = "'+self.PlayerUsername+'";' #relevant query to update coins
        cursor.execute(updatequery)
        databaseConnection.commit()
        cursor.close()
        databaseConnection.close()
        
    def ValidPrimaryKey(self, EnterredUsername):
        #database method: check validity of username
        databaseConnection = sqlite3.connect("Turbo90.db")
        cursor = databaseConnection.cursor()
        checkForExistingPrimaryKeyQuery = 'SELECT Username FROM Users WHERE Username = "'+EnterredUsername+'";' #relevant query to validate the username exists
        cursor.execute(checkForExistingPrimaryKeyQuery)
        ReturnedUsername = format(cursor.fetchone()) # fetchone just fetches the Username only (fetches one)
        databaseConnection.commit()
        cursor.close()
        databaseConnection.close()
        if ReturnedUsername == "None": #if no username has been returned the username not valid
            return False
        else:
            return True #username must exist so return true

    def Login(self, EnterredUsername, EnterredPassword, PlayerInfo):
        #database method: login process
        remove = [",", "(", ")", "'"]  #list of characters that need to be removed from returned value
        playerPWD = [] #list to store playerpwd
        playerCoins = [] # list to store playercoins
        databaseConnection = sqlite3.connect("Turbo90.db")
        cursor = databaseConnection.cursor()
        selectpwdquery = 'SELECT Password FROM Users WHERE Username = "'+EnterredUsername+'";'
        cursor.execute(selectpwdquery)
        Result1 = format(cursor.fetchone())
        Result1List = list(Result1)
        for index in Result1List: #removes all SQL operators/unnecessary characters
            if index not in remove:
                playerPWD.append(index)
        playerPWD = "".join(playerPWD) #turns into coherent string from list
        selectcoinsquery = 'SELECT Coins FROM Users WHERE Username = "'+EnterredUsername+'";'
        cursor.execute(selectcoinsquery)
        Result2 = format(cursor.fetchone())
        Result2List = list(Result2)
        for index in Result2List: #same process but with the coins
            if index not in remove:
                playerCoins.append(index)
        playerCoins = "".join(playerCoins)
        databaseConnection.commit()
        cursor.close()
        databaseConnection.close()
        HashedEnterredPWD = Hash.HashText(EnterredPassword)
        if playerPWD == HashedEnterredPWD: #compares enterred password with actual, if equal then pwd correct and login proceeds
            self.PlayerUsername = EnterredUsername #update username to true value
            PlayerInfo.GetData(EnterredUsername, int(playerCoins)) #update PlayerData() with new variables received from DB,
            return True  
        else:
            return False
    
    def DeleteRecord(self, EnterredUsername):
        databaseConnection = sqlite3.connect("Turbo90.db")
        cursor = databaseConnection.cursor()
        Deletequery = 'DELETE FROM Users WHERE Username = "'+EnterredUsername+'";'
        cursor.execute(Deletequery)
        databaseConnection.commit()
        cursor.close()
        databaseConnection.close()
