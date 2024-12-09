from entry import create_table,entry_data,generate_slip
from datetime import datetime

print("-----------parking ticket system--------------")
print(" 1) Create ")
print(" 2) Entry  ")

while True:
    choices = int(input("Enter your choices: "))

    if choices == 1:
        create_table()
        print("Database table created successfully")
    elif choices == 2:
        type_of_vehicle = None
        username = input("Enter the username: ")
        phone = input("Enter your phone number: ")
        vehicle_number = input("Enter your vehicle number: ")
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
        vehicle_type = int(input("Enter 1 for two wheeler and 2 for four wheeler: "))
        if vehicle_type == 1:
            type_of_vehicle = "two wheelers"
        elif vehicle_type == 2:
            type_of_vehicle = "four wheelers"
        else:
            print("Invalid choice for vehicle type")
        entry_data(username = username,phone = phone, vehicle_number = vehicle_number, vehicle_type = vehicle_type,type_of_vehicle = type_of_vehicle,formatted_datetime = formatted_datetime)
        generate_slip(username=username,vehicle_number = vehicle_number, entry_time = formatted_datetime)
        