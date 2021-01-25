import sqlite3
import time
def create(): 
    try:
        databaseNameInput = str(input("============================================\nType database name >>"))
        databaseName = databaseNameInput + ".db"
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        tableName = str(input("Table name (Can not be set as table)>>"))
        columnNumber = int(input("Number of columns >>"))
        if columnNumber == 1:
            columnName = str(input("Column name :"))
            tableCreate = "CREATE TABLE [" + tableName + "] ( [" + columnName + "] varchar(128))"
            cursor.execute(tableCreate)
        elif columnNumber < 1:
            print("Unable to create table with less than 1 column.")
            create()
        else:
            columnName = str(input("Column name :"))
            tableCreate = "CREATE TABLE [" + tableName + "] ( [" + columnName + "] varchar(128))"
            cursor.execute(tableCreate)
            for _ in range(0,(columnNumber-1)):
                columnName = str(input("Column name :"))
                columnAdd = "ALTER TABLE [" + tableName + "] ADD COLUMN [" + columnName + "] varchar(128)"
                cursor.execute(columnAdd)
        print("Database created successfully\nOpen manage.py to edit your database.")
        exitInput = input("Create another database? (y/n)>>")
        if exitInput == "y" or exitInput == "Y":
            create()
            connection.close()
        elif exitInput == "n" or exitInput == "N":
            connection.close()
            time.sleep(10)
    except:
        connection.close()
        print("Error.\nDelete the database file created (",databaseName,") and try again.")
        create()
create()
