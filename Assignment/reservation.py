import csv
import os

tables = [
    {
        "number": 1,
        "seats": 2,
    },
    {
        "number": 2,
        "seats": 4,
    },
    {
        "number": 3,
        "seats": 5,
    },
    {
        "number": 4,
        "seats": 6,
    },
    {
        "number": 5,
        "seats": 8,
    },
]

def view_tables():
    for table in tables:
        print(table)
view_tables()

reservation_file = "reservations.csv"


# Make reservations
def make_reservations(tables, reservation_file):
    # Prompt the users for their details
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter the number of people: "))
    date =input("Enter reservation date (YYYY-MM-DD): ")
    start_time = (input("Enter your starting time (HH:MM): "))
    end_time = (input("Enter your end time (HH:MM): "))

    # available_table = [table for table in tables if table["seats"] >= party_size and table["number"] not in reservation_file]

    available_table = [table for table in tables if table ["seats"] >= party_size]
    if not available_table:
        print("table not available for your party size")

    print("Available tables: ")
    for table in available_table:
        print(f"Table {table['number']} - seats: {table['seats']}")

    # prompt the user to enter the table number they want to reserve
    table_number = int(input("Enter table number to reserve: "))

    # Check if the entered table number is valid (i.e. it exists in the available table)
    if table_number not in [table['number'] for table in available_table]:
        print("invalid table number")
        return
    
    reservation = {"name" : name, "party_size" : party_size}
    print(f"Table {table_number} reserved successfully for {name}.")
    print(reservation)

    # create a new row for the reservation with the entered details
    new_row = [table_number, name, contact, party_size, date, start_time, end_time]

    # create a new header if header is not present
    header = ['table_number', 'name', 'party_size', 'date', 'start_time', 'end_time']
    try:
        # open the reservations file in append mode
        with open(reservation_file, 'a', newline='') as file:
            writer = csv.writer(file) #Create a CSV writer object
            # create/write header if not present
            if not header:
                writer.writerow(header)
                writer.writerow(new_row) #Write the new reservation to the file
            else:
                writer.writerow(new_row)

        # Print a success message
        print(f"Table {table_number} reserved successfully for {name} on {date} from {start_time} to {end_time}.")
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"Error making reservation: {e}")
        pass


# View reservations
def view_reservations(reservation_file):
    try:
        with open(reservation_file, 'r') as file:
            reader = csv.reader(file)
            reservations = list(reader)
            print(reservations)
            if reservations:
                for i in reservations:
                    print(i)
            else:
                ('No reservations found')
            pass
    except Exception as e:
        print(f"Error reading reservations: {e}")
        pass

#Cancel reservation
def cancel_reservation(reservation_file):
    name = input("Enter your name: ")
    reserved_date = input("Enter the date of reservation (YYYY-MM-DD): ")
    try:
        with open(reservation_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)

        current_reservation = [row for row in reservations if not (row[header.index('name')] == name and row[header.index('date')] == reserved_date)]
        with open(reservation_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(current_reservation)
            if len(current_reservation) == len(reservations):
                print("No matching reservation found.")
            else: 
                print(f"Reservation for {name} on {reserved_date} has been canceled.")
                pass
    except Exception as e:
        print(f"Error cancelling reservation: {e} ")

# daily summary
def daily_summary(reservation_file):
    date = input("Enter date of reservation: ")
    try:
        with open(reservation_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
            correct_reservations = [row for row in reservations if row[header.index("date")] == date]
            if correct_reservations:
                for i in correct_reservations:
                    print(i)
                else:
                    print("No reservation found")
    except Exception as e:
        print('Invalid date')
        pass


#modify reservation
def modify_reservation(reservation_file):
    date = input("Enter current reservation date (YYYY-MM-DD): ")
    name = input("Enter your current reservation name: ")
    # table_number = int(input("Enter table number to modify: "))
    with open(reservation_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        reservations = list(reader)
        # print(header)

    reservation_found = False
    for reservation in reservations:
        if reservation[header.index("date")] == date and reservation[header.index("Name")] == name: #and reservation[header.index("Table Number")] == table_number
            reservation_found = True
            print("Current reservation details: ", reservation)

            # update the inputs
            new_name = input(f"Enter new name (leave blank to keep current value '{reservation[header.index('name')]}'): ")
            if new_name: 
                reservation[header.index('name')] = new_name

            new_date = input(f"Enter new date (leave blank to keep current value '{reservation[header.index('date')]}'): ")
            if new_date: 
                reservation[header.index('date')] = new_date

            # new_table_number = input(f"Enter new table number (leave blank to keep current value '{reservation[header.index('table_number')]}'): ")
            # if new_table_number: 
                # reservation[header.index("table_number")] = new_table_number
        if reservation_found:
            # Write the updated reservations back to the CSV file 
            with open(reservation_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(reservations)
            print('Reservation updated successfully.')
        else:
            print("No reservation found for these details")
        return


#Function for display
def display():
    Reservations = reservation_file
    while True:
        print('Reservation System')
        print('1. Make reservation')
        print('2. View reservations')
        print('3. Cancel reservation')
        print('4. Modify reservation')
        print('5. Daily Summary')
        print('6. Exit')

        choice = input('select: ')
        if choice == '1':
            make_reservations(tables, reservation_file)
        elif choice == '2':
            view_reservations(reservation_file)
        elif choice == '3':
            cancel_reservation(reservation_file)
        elif choice == '4':
            modify_reservation(reservation_file)
        elif choice == '6':
              daily_summary(reservation_file)
        elif choice == '7':
            break
        else:
            print('Invalid choice')
display()





    
    