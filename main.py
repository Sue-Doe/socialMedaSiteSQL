from connection.connection import connectToServer

def main():
    try:
        connection= connectToServer()
        cursor = connection.execute("select * from users")
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
        connection.close()
    except Exception as e:
        print(f"Failed to connect to database: {e}")
main()