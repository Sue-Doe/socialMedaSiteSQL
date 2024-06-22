from connection.connection import connectToServer
from Login.userLogin import print_start_screen
from Tests.testUserCreation import runUserCreation




def main():
    try:

        print_start_screen()
    except Exception as e:
        print(f"Failed to connect to database: {e}")
main()