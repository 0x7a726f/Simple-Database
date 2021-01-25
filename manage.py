import sqlite3
def manage():
    def databaseEnter():
        try:
            global databaseName
            databaseName = str(input("Type database file name. e.g. database.db >>"))
            global connection
            connection = sqlite3.connect(databaseName)
            global cursor
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            global tableName
            tableName = str(cursor.fetchall())
            global remove
            remove = ["[","]","(",")",",","'"," "]
            remove2 = ["[","]","(",")","'",]
            tableName = ''.join(i for i in tableName if not i in remove)
            print("=====================================================\nTable :",tableName,"")
            cursorExecuteColumnName = "SELECT * FROM " + tableName
            cursor.execute(cursorExecuteColumnName)
            global columnList
            columnList = [member[0] for member in cursor.description]
            global columnNumber
            columnNumber = len(columnList)
            global columnShow
            columnShow = ' , '.join(r for r in columnList if not r in remove2)
            print("Columns :",columnShow,"\n=====================================================")
        except:
            print("Error.Try again.")
            databaseEnter()

    def userChoiceAsk():
        global userChoice
        userChoice = str(input("Add data (1)    |    Edit data (2) >>"))
        if userChoice == "1":
            addData()
        elif userChoice == "2":
            editData()
        else:
            print("Error.")
            userChoiceAsk()

    def addData():
        r = 0
        addList = []
        for _ in range(0,columnNumber):
            dataText = "Add data in table : " + columnList[r] + " >>"
            dataAdd = str(input(dataText))
            addList.append(dataAdd)
            r = r + 1
        addListTuple = tuple(addList)
        addListTuple = '" , "'.join(addListTuple)
        addListTuple = '"' + addListTuple + '"'
        executeAdd = "INSERT INTO " + tableName + " VALUES ( " + addListTuple + " )"
        cursor.execute(executeAdd)
        connection.commit()
        againInput = str(input("Data successfully added!\nAdd more data? (y/n) >>"))
        if againInput == "y" or againInput == "Y":
            addData()
        elif againInput == "n" or againInput == "N":
            userChoiceAsk()
        else:
            print("Error")
            databaseEnter()

    def editData():
        try:
            print("=====================================================\nColumns :",columnShow,)
            print("Select two columns to search from.")
            firstColumn = str(input("1st column >>"))
            secondColumn = str(input("2nd column >>"))
            a = "Type " + firstColumn + " value >>"
            firstColumnData = str(input(a))
            b = "Type " + secondColumn + " value >>"
            secondColumnData = str(input(b))
            columnSet = set(columnList)
            if firstColumn and secondColumn in columnSet:
                try:
                    selectExecute = "SELECT * FROM " + tableName + " WHERE " + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                    cursor.execute(selectExecute)
                    selectedRow = cursor.fetchall()
                    selectedRow = list(sum(selectedRow, ()))
                    s = 0
                    for _ in range(0,columnNumber):
                        print(columnList[s],": ",selectedRow[s])
                        s = s + 1
                except:
                    print("Data does not exist in these columns.Try again.")
                    editData()
                l = 0
                userInput = str(input("Edit data (1)    |    Delete row (2) >>"))
                if userInput == "1":
                    for _ in range(0,columnNumber):
                        a = "Change data in column " + columnList[l] + " (y/n) >>"
                        changeDataInput = str(input(a)) 
                        if changeDataInput == "y" or changeDataInput == "Y":
                            if columnList[l] == firstColumn:
                                changeData = str(input("Type data >>"))
                                changeDataExecute = "UPDATE " + tableName + " SET " + firstColumn + '="' + changeData + '" WHERE ' + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                                print(changeDataExecute)
                                cursor.execute(changeDataExecute)
                                connection.commit()
                                firstColumnDataExec = "SELECT " + firstColumn + " FROM " + tableName + " WHERE " + firstColumn + '="' + changeData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                                cursor.execute(firstColumnDataExec)
                                firstColumnData = str(cursor.fetchall())
                                firstColumnData = ''.join( _ for _ in firstColumnData if _ not in "[(')],")
                                print(firstColumnData)   
                            elif columnList[l] == secondColumn:
                                changeData = str(input("Type data >>"))
                                changeDataExecute = "UPDATE " + tableName + " SET " + secondColumn + '="' + changeData + '" WHERE ' + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                                cursor.execute(changeDataExecute)
                                connection.commit()
                                secondColumnDataExec = "SELECT " + secondColumn + " FROM " + tableName + " WHERE " + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + changeData + '"'
                                cursor.execute(secondColumnDataExec)
                                secondColumnData = str(cursor.fetchall())
                                secondColumnData = ''.join( _ for _ in secondColumnData if _ not in "[(')],")
                                print(secondColumnData)
                            else:
                                changeData = str(input("Type data >>"))
                                changeDataExecute = "UPDATE " + tableName + " SET " + columnList[l] + "=" + changeData + " WHERE " + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                                cursor.execute(changeDataExecute)
                                connection.commit()
                        else:
                            pass
                        l = l + 1
                    print("Edits successfully completed.")
                    userChoiceAsk()
                elif userInput == "2":
                    userInput2 = str(input("Are you sure? (y/n) >>"))
                    if userInput2 == "y" or userInput2 == "Y":
                        deleteExecute = "DELETE FROM " + tableName + " WHERE " + firstColumn + '="' + firstColumnData + '" AND ' + secondColumn + '="' + secondColumnData + '"'
                        cursor.execute(deleteExecute)
                        connection.commit()
                        print("Row deleted.")
                        editData()
                    elif userInput2 == "n" or userInput2 == "N":
                        editData()
                    else:
                        print("Error.Try again.")
                        editData()
                else:
                    print("Error.Try again.")
                    editData()
            else:
                print("Columns do not exist in the table.Try again.")
                editData()
        except:
            print("Error.Try again.")
            editData()

    databaseEnter()
    userChoiceAsk()
manage()
