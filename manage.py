import sqlite3
def manage():
    databaseName = str(input("Type database file name. e.g. database.db >>"))
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableName = str(cursor.fetchall())
    remove = ["[","]","(",")",",","'"," "]
    remove2 = ["[","]","(",")","'","O"]
    tableName = ''.join(i for i in tableName if not i in remove)
    print("-----------------------------------------------------\nTable :",tableName,"")
    cursorExecuteColumnName = "SELECT * FROM " + tableName
    cursor.execute(cursorExecuteColumnName)
    columnList = [member[0] for member in cursor.description]
    columnShow = ' , '.join(r for r in columnList if not r in remove2)
    print("Columns :",columnShow,"\n-----------------------------------------------------")
    userChoice = str(input("Add data (1)    |    Edit data (2) >>"))
    if userChoice == "1":
        print()
manage()
