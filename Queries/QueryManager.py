from connection.connection import connectToServer
from Account.User import User


class QueryManager:

    def __init__(self):
        self.connection = connectToServer()

    def createAccount(self,userInfo):
        try:
        # Create a cursor object
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users (username, password, first_name,last_name, birth_date, join_date, role)
                VALUES (?,?,?,?,?,?,?);
            """,userInfo)
            self.connection.commit()
        except Exception as e:
            print("Could not create Account:", e) 
            self.connection.rollback() 
        finally:
            print("Account Created Successfully")

    def checkCredentials(self,username,password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT user_id,username,first_name,last_name,birth_date,join_date,role FROM users WHERE username = ? AND password = ?;
                """, username,password)
            rows = cursor.fetchall()
            print(len(rows))
            if (len(rows) > 1):
                raise(Exception)
            elif (len(rows) == 1):
                return User(rows[0])
            elif (len(rows) == 0):
                return None
                

        except Exception as e:
            print("Error cannot login", e)


