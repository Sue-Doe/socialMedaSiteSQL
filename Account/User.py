class User:

    # def __init__(self,userID,username,firstName,lastName,dateOfbirth,dateJoined,role):
    #     self.userID = userID
    #     self.username = username
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.dateOfBirth = dateOfbirth
    #     self.dateJoined = dateJoined
    #     self.userRole = role
    def __init__(self,userInfo):
        self.userID = userInfo[0]
        self.username = userInfo[1]
        self.firstName = userInfo[2]
        self.lastName = userInfo[3]
        self.dateOfBirth = userInfo[4]
        self.dateJoined = userInfo[5]
        self.userRole = userInfo[6]
    def __str__(self):
        return f"Username: {self.username}"

    def getUsername(self):
        return self.username
    