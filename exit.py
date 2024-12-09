import sqlite3
from datetime import datetime

def vehicle_exit(vehicle_number):
    connection = sqlite3.connect("parking_db.db")
    cursor = connection.cursor()
    cursor.execute(f'select * from tb_parking where vehicle_number = {vehicle_number}')
    data = cursor.fetchone()
    exit_time = datetime.now()
    formatted_exit_time = exit_time.strftime("%Y-%m-%d %H:%M")
    if data:
        cursor.execute(f'update tb_parking set exit_time = ? where vehicle_number = ? ',(formatted_exit_time,vehicle_number))
        connection.commit()
    else:
        print("Please enter the correct vehicle number")

vehicle_exit(9090)