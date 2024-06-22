import getpass
from Queries.QueryManager import QueryManager
from Account.AccountManager import AccountManager
from datetime import datetime
import os
import platform


QUIT_VALUE = "3"
queryManager = QueryManager()
accountManager = AccountManager()

def clear_terminal():
    if platform.system() == "windows":
        os.system("cls")
    else:
        os.system("clear")



def print_start_screen():
    clear_terminal()

    login_art = """
    ******************************************************
    *                                                    *
    *          WELCOME TO THE REST OF YOUR LIFE          *
    *                                                    *
    ******************************************************
    *                                                    *
    *  1) Log In                                         *
    *  2) Create an Account                              *
    *  3) Quit                                           *
    *                                                    *
    ******************************************************
    """
    print(login_art)
    startSelector()


def print_login_screen():
    username = accountManager.getUsername()
    welcomeString = f"*                WELCOME {username}     "
    welcomeString = welcomeString.ljust(53, ' ') + "*"

    login_art = f"""
    ******************************************************
    *                                                    * 
    {welcomeString}
    *                                                    *
    ******************************************************
    *                                                    *
    *  1) View friends                                   *
    *  2) Search Username                                *
    *                                                    *
    *                                                    *
    *                                                    *
    *                                                    *
    *                                                    *
    *                                                    *
    ******************************************************
    """
    print(login_art)
    userSelector()

    
def startSelector():
    seclector = input("Please make a selection > ")

    while (seclector != QUIT_VALUE):
        if (seclector == "1"):
            login()
            break
        elif (seclector == "2"):
            createAccount()
            break
        else:
            seclector = input("Please make a selection > ")


def userSelector():

    seclector = input("Please make a selection > ")

    while (seclector != QUIT_VALUE):
        if (seclector == "1"):
            login()
            break
        elif (seclector == "2"):
            createAccount()
            break
        else:
            seclector = input("Please make a selection > ")



def login():
    username = input("Please enter your username > ")
    password = getpass.getpass("Please enter your password > ")
    loggedInUser = queryManager.checkCredentials(username,password)
    if (loggedInUser != None):
        accountManager.loginUser(loggedInUser)
        accountManager.printCurrUserInfo()
        clear_terminal()
        print_login_screen()
    else:
        print("Sorry Incorrect Username/Password")        



def createAccount():
    username =  input("Please enter a username > ")

    password = "1"
    passwordConfirm= "2"
    while (password != passwordConfirm):
        password = getpass.getpass("Please enter your password > ")
        passwordConfirm =   getpass.getpass("Please confirm password > ")

    firstname =  input("Please enter your first name > ")
    lastname = input("Please enter your last name > ")
    dateOfbrith = input("Please enter your date of birth (YYYY-MM-DD) > ")

    currentDay = datetime.now()


    infoList = [username,password,firstname,lastname,dateOfbrith,currentDay.strftime("%Y-%m-%d"), "USER"]
    queryManager.createAccount(infoList)        
    print(infoList)
