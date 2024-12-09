import sqlite3

def create_table():
    connection = sqlite3.connect("parking_db.db")
    cursor = connection.cursor()
    cursor.execute('create table if not exists tb_parking (id integer primary key autoincrement, username varchar(200), phone varchar(13), vehicle_number varchar(10) not null unique, entry_time varchar(200), exit_time varchar(200), total_price varchar(30), vehicle_type varchar(100))')
    connection.commit()
    connection.close()

def entry_data(**kwargs):
    connection = sqlite3.connect("parking_db.db")
    cursor = connection.cursor()
    
    insert_query = "insert into tb_parking (username, phone, vehicle_number, entry_time, exit_time, total_price, vehicle_type) values(?, ?, ?, ?, ?, ?, ?)"
    val = [(kwargs['username'],kwargs['phone'],kwargs['vehicle_number'],kwargs['formatted_datetime'],"","",kwargs['type_of_vehicle'])]
    cursor.executemany(insert_query,val)
    connection.commit()
    connection.close()


def generate_slip(username,vehicle_number, entry_time):
    with open(f"generated_slip/{username}.txt",'w') as f:
        f.writelines([
            f"Name : {username}\n",
            f"Vehicle number : {vehicle_number}\n",
            f"Entry Time : {entry_time}\n"
        ])
    print("slip generate successfully. Collect the slip")