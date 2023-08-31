"""
-----------------------------------------------
File: GUI_Functions.py
Authors: Group 40
Course: CP363
Date: 2023-03-26
-----------------------------------------------
"""


import mysql.connector

# Function to connect to MySQL database
def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="sqluser",
        password="password",
        database="hotelmanagement"
    )
    return connection

# Function to drop tables
def drop_all_tables():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    DROP TABLE IF EXISTS 
    Employee, Department, Hotel, HotelContact, 
    Guest, Booking, Room, RoomType, 
    RoomPrice, Service_type""")
    connection.commit()
    cursor.close()
    connection.close()
    print("All tables dropped successfully")

# Function to create tables
def create_tables():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Hotel (
            hotel_id INT PRIMARY KEY,
            hotel_name VARCHAR(50) NOT NULL,
            location VARCHAR(100) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS HotelContact (
            hotel_id INT PRIMARY KEY,
            hotel_phone_number VARCHAR(20) NOT NULL,
            hotel_email VARCHAR(20) NOT NULL,
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RoomType (
            roomtype_id INT PRIMARY KEY,
            room_type VARCHAR(50) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RoomPrice (
            roomtype_id INT PRIMARY KEY,
            hotel_id INT,
            room_price DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (roomtype_id) REFERENCES RoomType(roomtype_id),
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Room (
            room_id INT PRIMARY KEY,
            hotel_id INT NOT NULL,
            roomtype_id INT,
            requests VARCHAR(100),
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
            FOREIGN KEY (roomtype_id) REFERENCES RoomType(roomtype_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Guest (
            guest_id INT PRIMARY KEY,
            guest_name VARCHAR(50) NOT NULL,
            guest_email VARCHAR(50) NOT NULL,
            guest_phone_number VARCHAR(50) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Booking (
            booking_id INT NOT NULL,
            guest_id INT NOT NULL,
            room_id INT NOT NULL,
            guest_name VARCHAR(100),
            amount_paid DECIMAL(10,2),
            checkin_date DATE,
            checkout_date DATE,
            service_description VARCHAR(100),
            PRIMARY KEY (booking_id, room_id),
            FOREIGN KEY (guest_id) REFERENCES Guest(guest_id),
            FOREIGN KEY (room_id) REFERENCES Room(room_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            department_ID INT PRIMARY KEY,
            dept_name VARCHAR(50)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            employee_id INT PRIMARY KEY,
            department_id INT,
            employee_name VARCHAR(50),
            job_title VARCHAR(50),
            contact VARCHAR(20),
            hotel_id INT,
            FOREIGN KEY (department_id) REFERENCES Department(department_id),
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Service_Type (
            service_type_id INT PRIMARY KEY,
            service_description VARCHAR(100),
            amount DECIMAL(10,2),
            service_date DATE,
            room_id INT,
            FOREIGN KEY (room_id) REFERENCES Room(room_id)
        )
    """)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Tables created successfully")

# Function to populate tables
def populate_tables():
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO Hotel VALUES (123, 'Embassy', 'Toronto')")
    
    cursor.execute("""
        INSERT INTO Hotel (hotel_id, hotel_name, location)
        VALUES 
        (100, 'Chateau Lake Louise', 'Alberta'),
        (101, 'The Fairmont Banff Springs', 'Alberta'),
        (102, 'The Fairmont Chateau Whistler', 'British Columbia'),
        (103, 'The Fairmont Jasper Park Lodge', 'Alberta')
    """)
    cursor.execute("""
        INSERT INTO HotelContact (hotel_id, hotel_phone_number, hotel_email)
        VALUES 
        (100, '123-456-7890', 'hotel1@gmail.com'),
        (101, '987-654-3210', 'hotel2@gmail.com'),
        (102, '555-123-4567', 'hotel3@gmail.com'),
        (103, '444-555-6666', 'hotel4@gmail.com')
    """)
    
    cursor.execute("""
        INSERT INTO Guest (guest_id, guest_name, guest_email, guest_phone_number)
        VALUES
        (100, 'John Doe', 'johndoe@email.com', '123-456-7890'),
        (101, 'Jane Doe', 'janedoe@email.com', '123-456-7890'),
        (102, 'John Smith', 'johnsmith@email.com', '123-456-7890'),
        (103, 'Jane Smith', 'janesmith@email.com', '123-456-7890')
    """)
    
    cursor.execute("""
        INSERT INTO RoomType (roomtype_id, room_type)
        VALUES 
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Suite'),
        (4, 'Single')
    """)

    cursor.execute("""
        INSERT INTO RoomPrice (roomtype_id, hotel_id, room_price)
        VALUES 
        (1, 100, 80.00),
        (2, 101, 90.00),
        (3, 102, 100.00),
        (4, 103, 80.00)
    """)
    
    cursor.execute("""
        INSERT INTO Room (room_id, hotel_id, roomtype_id, requests)
        VALUES
        (101, 100, 1,'Room Service' ),
        (102, 101, 2, 'Bar Service'),
        (103, 102, 3, 'Restaurant Service'),
        (104, 103, 4, 'Long Distance Call')
    """)
    
    cursor.execute("""
        INSERT INTO Department (department_id, dept_name)
        VALUES
        (100, 'Reception'),
        (101, 'Room-service'),
        (102, 'Management'),
        (103, 'Kitchen')
    """)
    
    cursor.execute("""
        INSERT INTO Employee (employee_id, department_id, employee_name, job_title, contact, hotel_id)
        VALUES
        (100, 100, 'Jane Doe', 'Receptionist', '555-555-1216', 100),
        (101, 101, 'John Smith', 'Room-service', '555-555-1217', 100),
        (102, 102, 'Jane Smith', 'Manager', '555-555-1218', 100),
        (103, 103, 'John Doe', 'Chef', '666-666-3434', 100)
    """)
    
    cursor.execute("""
        INSERT INTO Service_Type (service_type_id, service_description, amount, service_date) VALUES 
        (1, 'Room Service', 50.00,'2023-03-12'), 
        (2, 'Bar Service', 80.00,'2023-03-25'), 
        (3, 'Restaurant Service', 60.00,'2023-06-15'), 
        (4, 'Long Distance Call', 10.00,'2023-02-12')
    """)
    
        # Insert Booking data
    cursor.execute("""
    INSERT INTO Booking (booking_id, guest_id, room_id, guest_name, amount_paid, checkin_date, checkout_date, service_description) VALUES 
    (100, 100, 101, 'John Doe', 100.00, '2022-01-01', '2022-01-02', 'Room Service'), 
    (101, 100, 101, 'Jane Doe', 90.00, '2022-01-03', '2022-01-04', 'Bar Service'), 
    (102, 101, 102, 'John Smith', 80.00,'2022-01-05', '2022-01-06', 'Restaurant Service'), 
    (103, 101, 103, 'Jane Smith', 80.00, '2022-01-07', '2022-01-08', 'Long Distance Call')
    """)
    
    
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Tables populated successfully")

def query_all_tables():
    connection = connect()
    cursor = connection.cursor()
    results = []

    
    # Query 1: Using EXISTS to check for guest with bookings
    cursor.execute("SELECT * FROM hotel")
    print("Query 1: Guests with Bookings")
    results.append("Hotel")
    results.append(cursor.fetchall())
    
    

    # Query 2: Using UNION to combine guest names and department names
    cursor.execute("SELECT * FROM hotelcontact")
    print("Query 2: Guest and Rooms")
    results.append("Hotel_Contact")
    results.append(cursor.fetchall())

    # Query 3: Using ORDER_BY to find hotels in Toronto
    cursor.execute("SELECT * FROM room")
    print("Query 3: Available Locations in Toronto")
    results.append("Room")
    results.append(cursor.fetchall())

    # Query 4: Using COUNT to find the number of bookings for each guest
    cursor.execute("SELECT * FROM roomtype")
    print("Query 4: Number of bookings for each guest")
    results.append("RoomType")
    results.append(cursor.fetchall())

    # Query 5: Using GROUP BY and HAVING to find guests with multiple bookings
    cursor.execute("SELECT * FROM roomprice")
    print("Query 5:  Guests with multiple bookings")
    results.append("RoomPrice")
    results.append(cursor.fetchall())

    # Query 6: Using GROUP BY and HAVING to find rooms with multiple bookings
    cursor.execute("SELECT * FROM guest")
    print("Query 6: Rooms with Multiple Bookings")
    results.append("Guest")
    results.append(cursor.fetchall())

    # Query 7: Using GROUP BY and HAVING to find hotels with a high occupancy rate
    cursor.execute("SELECT * FROM department")
    print("Query 7: Hotels with High Occupancy Rates")
    results.append("Department")
    results.append(cursor.fetchall())
    
    # Query 8: Using UNION to combine guest names and service descriptions
    cursor.execute("SELECT * FROM employee")
    print("Query 8: Employee and Service Descriptions")
    results.append("Employee")
    results.append(cursor.fetchall())
    
# Query 9: Using MINUS to find rooms that have not been booked
    cursor.execute("SELECT * FROM booking")
    print("Query 9: Available Rooms")
    results.append("Booking")
    results.append(cursor.fetchall())

# Query 10: Using MINUS to find rooms that have not been booked
    cursor.execute("SELECT * FROM service_type")
    print("Query 9: Available Rooms")
    results.append("Service_Type")
    results.append(cursor.fetchall())
    
    cursor.close()
    connection.close()
    return results

def get_table_names():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SHOW Tables")
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result

def query_table(table_name):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM `{table_name[0]}`")
    table_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return table_data



def delete_record(table_name, record_id):
    try:
        connection = connect()
        cursor = connection.cursor()
        # Delete an existing record from a table in the database
        cursor.execute("DELETE FROM {} WHERE {}_id=%s".format(table_name[0], table_name[0]), (record_id,))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

def search_record(table_name, record_id):
    try:
        connection = connect()
        cursor = connection.cursor()
        if table_name[0] == "roomprice":
            table_name[0] = "roomtype"
        # Search an existing record from a table in the database
        query = f"SELECT * FROM {table_name[0]} WHERE {table_name[0]}_id = {record_id}"
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
        return result
