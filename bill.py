import sqlite3
# create fare table
# vehicle type
# base fare 
# additional fare

def vehicle_type(choices):
    if choices == '1':
        return "two wheelers"
    elif choices == '2':
        return "four wheelers"
    else:
        print("invalid choices")


def create_fare_table():
    connection = sqlite3.connect("parking_db.db")
    cursor = connection.cursor()
    cursor.execute('create table if not exists tb_fare (vehicle_type varchar(100), base_fare varchar(4), additional_fare varchar(4))')
    print("fare table created successfully")
    connection.commit()
    connection.close()

# create_fare_table()

def insert_fare_data():
    connection = sqlite3.connect("parking_db.db")
    cursor = connection.cursor()
    insert_query = 'insert into tb_fare (vehicle_type, base_fare, additional_fare) values(?, ? ,?)'
    choice = input("Enter the 1 for two wheeler and 2 for four wheeler: ")
    type_of_vehicle = vehicle_type(choice)
    if type_of_vehicle == "two wheelers":
        base_fare = input("Enter the base fare: ")
        additional_fare = input("Enter the additional fare: ")
        cursor.execute(insert_query,(type_of_vehicle,base_fare,additional_fare))
    elif type_of_vehicle == "four wheelers":
        base_fare = input("Enter the base fare: ")
        additional_fare = input("Enter the additional fare: ")
        cursor.execute(insert_query,(type_of_vehicle,base_fare,additional_fare))
    else:
        print("Failed to insert fare table")
    connection.commit()
    connection.close()
    

# insert_fare_data()




