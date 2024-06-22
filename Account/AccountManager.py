class AccountManager:

    def __init__(self):
        self.loggedInUser = None

    def loginUser(self,user):
        self.loggedInUser = user


    def printCurrUserInfo(self):
        print(self.loggedInUser)

    def getUsername(self):
        if (self.loggedInUser):
            return self.loggedInUser.getUsername()
        else:
            return "Error: Name not found"
