import sqlite3
def manage():
    databaseName = str(input("Type database file name. e.g. database.db :\n"))
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableName = str(cursor.fetchall())
    remove = ["[","]","(",")",",","'"," "]
    tableName = ''.join(i for i in tableName if not i in remove)
    print("Table :",tableName)
    userChoice = str(input("Add data (1) | Edit data (2)"))
    if userChoice == "1":
        print()
manage()
