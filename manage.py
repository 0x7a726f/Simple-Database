import sqlite3
import time
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
    columnNumber = len(columnList)
    columnShow = ' , '.join(r for r in columnList if not r in remove2)
    print("Columns :",columnShow,"\n-----------------------------------------------------")
    userChoice = str(input("Add data (1)    |    Edit data (2) >>"))
    if userChoice == "1":
        r = 1
        addList = ["0"]
        for i in range(0,(columnNumber-1)):
            dataText = "Add data in table : " + columnList[r] + " >>"
            addData = str(input(dataText))
            addList.append(addData)
            r = r + 1
        addListTuple = tuple(addList)
        addListTuple = ' , '.join(addListTuple)
        print(addListTuple)
        executeAdd = "INSERT INTO " + tableName + " VALUES ( " + addListTuple + " )"
        cursor.execute(executeAdd)
        connection.commit()
        time.sleep(100)
    else:
        print("")
        
manage()
