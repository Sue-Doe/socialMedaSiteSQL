from connection.connection import connectToServer

def runUserCreation():
    print("Starting tests")
    
    # Establish the connection
    connection = connectToServer()
    
    try:
        # Create a cursor object
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, birth_date, join_date, role)
            VALUES ('cletus', 'ella', '1974-09-14', '2024-06-24', 'user');
        """)
    
        connection.commit()
    
    except Exception as e:
        print("An error occurred:", e) 
        connection.rollback() 
    
    finally:
        connection.close()

