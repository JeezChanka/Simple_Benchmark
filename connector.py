def CreateTableHandler(cnx): 
    cursor = cnx.cursor()
    # create table
    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS results ( 
                                Id int(11) AUTO_INCREMENT PRIMARY KEY,
                                Name varchar(250) NOT NULL,
                                Result float NOT NULL) """

    cursor.execute(mySql_Create_Table_Query)
    print("Results table created successfully")
    
    # insert dummy data

    # name = ["ADATA","ADATA","ADATA","Gigabyte","Intel","Goodram","HyperX","Patriot","Samsung","Odra"]
    # time = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    # mySql_Insert_Query = "INSERT INTO results (Name, result) VALUES (%s, %s)"
    # values = []
    # for i in range(0, len(name), 1):
    #     values.append((name[i], float(time[i])))
    # cursor.executemany(mySql_Insert_Query, values)
    # cnx.commit()
    
    cursor.close()
    

def GetDataHandler(cnx):  
    cursor = cnx.cursor()   
    # get data
    mySql_Select_Query = "SELECT * FROM results ORDER BY Id DESC LIMIT 10"
    cursor.execute(mySql_Select_Query)
    results = cursor.fetchall()

    # print("Recieved data:")
    # Loop through results and print
    # for result in results:
    #     print(result)
    
    cursor.close()
    return results
    
    
def InsertDataHandler(cnx, value): 
    cursor = cnx.cursor()
    #insert value into results

    mySql_Insert_Query = "INSERT INTO results (Name, result) VALUES (%s, %s)"
    cursor.execute(mySql_Insert_Query, value)
    cnx.commit()
    cursor.close()