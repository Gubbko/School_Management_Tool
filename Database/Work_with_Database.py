import sqlite3


# ----------------------------------------------------------------------------------------------------------
# -----Functions--------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

""" Connect to database
# This function requires the following parameters:
#       - Name of database file with it directory
# This function returns following parameters:
#       - connection to database
#       - cursor of database
"""
def connect_to_database(database_file_name):
    connection = sqlite3.connect(database_file_name)
    cursor = connection.cursor()
    return connection, cursor

""" Create table for database
# This function requires the following parameters:
#       - Cursor of database
#       - Name of new table
#       - Atributes of new table
"""
def Create_table(cursor, table_name, table_atributes):
    cursor.execute(f"CREATE TABLE {table_name} ({table_atributes})")

""" Insert new data to the table of database
# This function requires the following parameters:
#       - Connection to database
#       - Cursor of database
#       - Name of working table
#       - Data to insert to the table
"""
def Insert_data(connection, cursor, table_name, inserting_data):
    number_of_vaues = 5
    question_marks = ''
    for _ in range(number_of_vaues):
        question_marks += f"{question_marks}?,"
    question_marks = question_marks[:-1]
    values = "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    res = cursor.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    res.fetchone() is None
    cursor.execute(f"insert into {table_name} {values}", inserting_data)
    connection.commit()

def Read_database(connection, cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    results = cursor.fetchall()
    print("--- Data from Database ---")
    for result in results:
        print(result)
    connection.commit()

def Remove_Item_from_Database(connection, cursor, table_name, class_to, value):
    sql = f'DELETE FROM {table_name} WHERE {class_to}=?'
    cursor.execute(sql, (f"{value}",))
    connection.commit()



# ----------------------------------------------------------------------------------------------------------
# -----Main code--------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------



connection, cursor = connect_to_database("IT_Park.db")
# Execute a query
Remove_Item_from_Database(connection, cursor, "IT_Product", "Klass", "")

Read_database(connection, cursor, "IT_Product")



#connection, cursor = connect_to_database("IT_Park.db")
#Create_table(cursor, "IT_Product","Ev, Bilansikont, Klass, Varanr, Alamnr, Invnr, Varakirjeldus, KapitKp, Soetusmaksumus, Kulum perioodini, Jääkvper, Aadress, Aadressi text, Ruum, Kogus, Ühik, Töötaja, Eesnimi, Perenimi, L, Vastutav isik, Inventuuri kpseisuga, Invmärkus, Yes")

"""
inserting_data = ['HP','LJ','Prinet', 2562 , 163169 , 'A109', '11.01.2023']

connection, cursor = connect_to_database("IT_Park.db")
#Create_table(cursor, "IT_Product","Manufacture, Model, Product_type, Serial_Number, Inventuur_number, Class, Last_Invetarisation_Date")
#Insert_data(connection, cursor, "IT_Product", inserting_data)

cursor.execute("select * from IT_Product where Product_type=:c", {"c": "Lyberty City"})
IT_search = cursor.fetchall()
print(IT_search)

# Show table
cursor.execute("SELECT * FROM IT_Product")
#print(cur.description)

# ----------------------------------------------------------------------------------------------------------
# -----Final show of results--------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

for i in cursor.execute("select * from IT_Product"):
    print(i)


# ----------------------------------------------------------------------------------------------------------
# -----Ending of program------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

connection.close()
"""