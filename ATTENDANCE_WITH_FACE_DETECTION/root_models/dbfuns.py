import sqlite3 as lite

# connect to the database
def connect_fun(database_name):
    try:
        conn = lite.connect(database_name)
        return conn
    except lite.Error as e:
        print(e)

# To execute sql query
def execute_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return True
    except lite.Error as e:
        pass



#To create table
def create_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = "table created successfully"
        return result
    except lite.Error as e:
        print(e)
        print("this is error")
# insert one record into table
def insert_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()  # saves the data onto the disk
        return True
    except lite.Error as e:
        return print(e,'in insert function')



# fetch all records from table
def fetchall_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except lite.Error as e:
        print(e)

# fetch one record from table
def fetchone_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except lite.Error as e:
        print(e,'here in fetch one')
# update one record in the table
def update_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit() # saves the data onto the disk
    except lite.Error as e:
        print(e)

# delete one record from table
def delete_fun(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit() # saves the data onto the disk
    except lite.Error as e:
        print(e)

# close the connection
def close_fun(connection):
    try:
        connection.close()
    except lite.Error as e:
        print(e)






