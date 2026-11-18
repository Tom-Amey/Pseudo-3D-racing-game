from tkinter import *

class LoginPage():
    def __init__(self, SQLMethods):
        self.window = Tk()#initialising window
        self.window.title('Login Page')#window title
        self.window.geometry('700x500+400+0')#window size add plus starting x and starting y value to the size of the screen must have an arguement for both y and x to function correctly
        self.window['bg'] = '#7ed957'
        self.window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1) #configuring the rows and columns givign them a number
        self.window.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        #Loading Image
        self.logoImg = PhotoImage(file = "logoSmaller.png")
        self.CurrentStatusTxt = "" #for response to a user's action
        #creating Labels
        self.HelpText = Label(text = """Once finished, close the 
                            window to return to the game!""", bg='#7ed957')
        self.CurrentUserMessage = Label(text="""For Current Users:
                           Enter your Username and 
                           Password and click login.""", bg='#7ed957')    
        self.UsernameMessage = Label(text="Username", bg='#7ed957')
        self.PasswordMessage = Label(text="Password", bg='#7ed957')
        self.NewUserMessage = Label(text="""For New Users:
                             Enter a Username and Password 
                             that you wish to use and then 
                          click create account. Your 
                          profile will then be made.""", bg='#7ed957')
        self.LogoImgLabel = Label(self.window, image= self.logoImg, bg='#7ed957')
        #storing Stringvar for entry widgets
        self.Usernametext = StringVar()
        self.Passwordtext = StringVar()
        # creating Entry Widgets
        self.entryUsername = Entry(self.window, textvariable=self.Usernametext)
        self.entryPassword = Entry(self.window, textvariable=self.Passwordtext)
        self.instance = SQLMethods # initiating the SQLMethods for use in login page


    def InitiateCreateAccount(self):
        Username = self.Usernametext.get() # both get text enterred into the entry boxes
        Password = self.Passwordtext.get()
        #checking that the username does not exist by searching all primary keys in table
        if not self.instance.ValidPrimaryKey(Username):
            self.instance.AddNewRecord(Username, Password)
            self.CurrentStatusTxt = "Created Account! Please login."
        else:
            self.CurrentStatusTxt = "Username already in use.      "
        StatusLabel = Label(text=self.CurrentStatusTxt, bg='#7ed957')
        StatusLabel.grid(row=1, column=1, sticky="n", rowspan=1)
    
    def Policy(self):
        #displaying GDPR rules in seperate window
        policy = Toplevel()
        policy.geometry("300x300+400+0")
        policy.title = "Privacy Policy"
        policycontent = """How We Use Your Data?
        We collect information to personalise your
        experience with us at Turbo90. By clicking create
        account you agree to share the entered data 
        with us. We store coin score, username and 
        your password once hashed.
        Your data will always be stored locally and 
        securely in our database along with any other 
        users that play on this device.
        We promise not to use any of your information 
        for marketing purposes. The only individuals
        authorised to access your account is you and
        system administrators. 
        Under Article 17 of the UK GDPR legislation you, 
        the user has the "right to be forgotten", by 
        pressing delete account no information will 
        remain in the local database.
        Once you are finished reading close the window :)"""
        policylabel = Label(policy, text = policycontent)
        policylabel.pack() #pushing label to the window
        

    def AttemptLogin(self, PlayerInfo):
        # get the text from the entry widget
        Username = self.Usernametext.get()
        Password = self.Passwordtext.get()
        if self.instance.ValidPrimaryKey(Username): #if SQLMethods returns that the enterred primary key/username exists
            if self.instance.Login(Username, Password, PlayerInfo):
                self.CurrentStatusTxt = "       Successful Login!               "
            else:
                self.CurrentStatusTxt = "Incorrect Password!           "
        else:
            self.CurrentStatusTxt = "Username not Found.           "
            
        StatusLabel = Label(text=self.CurrentStatusTxt, bg='#7ed957')
        StatusLabel.grid(row=1, column=1, sticky="n", rowspan=1)
    
    def DeleteAccount(self):
        Username = self.Usernametext.get()
        self.instance.DeleteRecord(Username)
        self.CurrentStatusTxt = "      Account Deleted        "
        StatusLabel = Label(text=self.CurrentStatusTxt, bg='#7ed957')
        StatusLabel.grid(row=1, column=1, sticky="n", rowspan=1)
    def CreateLoginWindow(self, PLayerInfo):
    
        # bind the return key to the on_enter function
        self.entryUsername.bind("<Return>", self.AttemptLogin)
        self.entryPassword.bind("<Return>", self.AttemptLogin)

        #Creating the Buttons
        self.LoginButton = Button(self.window, text="Login", command= lambda: self.AttemptLogin(PLayerInfo))
        self.PrivacyPolicyButton = Button(self.window, text = "Privacy Policy", background="red", bd = 5, command = self.Policy)
        self.CreateAccountButton = Button(self.window, text = "Create Account", background="red", bd = 5, command = self.InitiateCreateAccount)
        self.DeleteAccountButton = Button(self.window, text = "Delete Account", background="red", bd = 5, command = self.DeleteAccount)
        #Placing all created assets on grid/window with row and column position and where they are in that square with any offset in y or x (pady/padx)
        self.LoginButton.grid(row = 4, column = 3, sticky="n", rowspan= 1, pady = 20)
        self.PrivacyPolicyButton.grid(row=1, column=4, sticky="n")
        self.CreateAccountButton.grid(row = 4, column = 3, sticky="s", rowspan= 1, pady=20)
        self.DeleteAccountButton.grid(row=2, column=4, sticky = "n", rowspan=1)
        self.UsernameMessage.grid(row = 2, column=3, sticky="n", rowspan=1)
        self.PasswordMessage.grid(row = 3, column=3, sticky="n", rowspan=1)
        self.CurrentUserMessage.grid(row = 3, column=1, sticky="n", rowspan=1)
        self.HelpText.grid(row=0, column=3, sticky="s", rowspan=1)
        self.NewUserMessage.grid(row=4, column=1, sticky="n", rowspan=1)
        self.LogoImgLabel.grid(row=2, column=1, sticky="n", rowspan=1)
        self.entryUsername.grid(row = 2, column = 3, sticky="n", rowspan= 1, pady=25)
        self.entryPassword.grid(row = 3, column = 3, sticky="n", rowspan=1, pady=25)
        self.window.mainloop() # must have this to run a window
