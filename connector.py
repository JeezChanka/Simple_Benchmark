import mariadb

def DataHandler():    
    # Connect to the database
    cnx = mariadb.connect(user='root', 
                        password='',
                        host='localhost',
                        port=3306,
                        database='benchmark')

    # Create a cursor object
    cursor = cnx.cursor()

    #create table

    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS results ( 
                                Id int(11) AUTO_INCREMENT PRIMARY KEY,
                                Name varchar(250) NOT NULL,
                                Result float NOT NULL) """

    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

    #insert data

    query = "INSERT INTO results (Name, result) VALUES (%s, %s)"
    values = ("ADATA", "43")
    cursor.execute(query, values)

    # Make sure data is committed
    cnx.commit()

    # Execute a query
    query = "SELECT * FROM results"
    cursor.execute(query)

    # Fetch results
    results = cursor.fetchall()

    # Loop through results and print
    for result in results:
        print(result)

    # Close cursor and connection
    cursor.close()
    cnx.close()