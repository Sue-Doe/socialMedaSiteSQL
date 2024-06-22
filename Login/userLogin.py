from Queries.QueryManager import QueryManager
from datetime import datetime

QUIT_VALUE = "3"
queryManager = QueryManager()

def print_login_screen():
    login_art = """
    ******************************************************
    *                                                    *
    *          WELCOME TO THE REST OF YOUR LIFE          *
    *                                                    *
    *  1) Log In                                         *
    *  2) Create an Account                              *
    *  3) Quit                                           *
    *                                                    *
    ******************************************************
    """
    print(login_art)
    startSelector()


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


def login():
    username = input("Please enter your username > ")
    password = input("Please enter your password > ")


def createAccount():
    username =  input("Please enter a username > ")

    password = "1"
    passwordConfirm= "2"
    while (password != passwordConfirm):
        password = input("Please enter your password > ")
        passwordConfirm =   input("Please confirm password > ")

    firstname =  input("Please enter your first name > ")
    lastname = input("Please enter your last name > ")
    dateOfbrith = input("Please enter your date of birth (YYYY-MM-DD) > ")

    currentDay = datetime.now()


    infoList = [username,password,firstname,lastname,dateOfbrith,currentDay.strftime("%Y-%m-%d"), "USER"]
    queryManager.createAccount(infoList)        
    print(infoList)
