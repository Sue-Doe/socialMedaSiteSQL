from connection.connection import connectToServer



class QueryManager:

    def __init__(self):
        self.connection = connectToServer()

    def createAccount(self,userInfo):
        cursor = self.connection.cursor()

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




