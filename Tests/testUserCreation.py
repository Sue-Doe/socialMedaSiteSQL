import pyodbc
import time
import json


def loadConfig():
    with open('../config.json','r') as file:
        config = json.load(file)
        return config



def main():
    config = loadConfig()
    server = config['server']
    database = config['database']
    username = config['username']
    password = config['password']
    connection_string = (
        f"Driver={{ODBC Driver 18 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )

    retry_attempts = 3
    for attempt in range(retry_attempts):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM USERS")
            row = cursor.fetchone()
            while row:
                print(row)
                row = cursor.fetchone()
            connection.close()
            break
        except pyodbc.Error as ex:
            print(f"Attempt {attempt + 1} failed: {ex}")
            if attempt < retry_attempts - 1:
                time.sleep(5)  # Wait for 5 seconds before retrying

if __name__ == "__main__":
    main()
