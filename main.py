from connection.connection import connectToServer
from Login.userLogin import print_login_screen
from Tests.testUserCreation import runUserCreation




def main():
    try:
        print_login_screen()
        # runUserCreation()

    except Exception as e:
        print(f"Failed to connect to database: {e}")
main()