use hotelmanagement;


CREATE TABLE Hotel ( -- Modified to remove non atomic values
  hotel_id INT PRIMARY KEY,
  hotel_name VARCHAR(50) NOT NULL,
  location VARCHAR(100) NOT NULL
);

CREATE TABLE HotelContact ( -- Modified to remove non atomic values
  hotel_id INT PRIMARY KEY,
  hotel_phone_number VARCHAR(20) NOT NULL,
  FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

CREATE TABLE RoomType ( -- Modified to remove partial dependencies
  roomtype_id INT PRIMARY KEY,
  room_type VARCHAR(50) NOT NULL
);

CREATE TABLE RoomPrice ( -- Modified to remove partial dependencies
  roomtype_id INT PRIMARY KEY,
  hotel_id INT,
  room_price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (roomtype_id) REFERENCES RoomType(roomtype_id),
  FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

CREATE TABLE Room ( -- Modified hotel_id and roomtype_id by making both of them non-null.
  room_id INT PRIMARY KEY,
  hotel_id INT NOT NULL,
  roomtype_ID INT NOT NULL,
  requests VARCHAR(100),
  FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
  FOREIGN KEY (roomtype_id) REFERENCES RoomType(roomtype_id)
);

CREATE TABLE Guest ( -- split guest_contact_info into two attributes: guest_email and guest_phone_number to remove transitive dependency.
  guest_id INT PRIMARY KEY,
  guest_name VARCHAR(20) NOT NULL,
  guest_email VARCHAR(50) NOT NULL,
  guest_phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE Booking ( -- Already in 3NF as each non-key attribute is dependent on the primary key and there are no transitive dependencies.
  booking_id INT NOT NULL,
  guest_id INT NOT NULL,
  room_id INT NOT NULL,
  guest_name VARCHAR(100),
  amount_paid DECIMAL(10,2),
  checkin_date DATE,
  checkout_date DATE,
  service_description VARCHAR(100),
  PRIMARY KEY (booking_id, room,_id),
  FOREIGN KEY (guest_id) REFERENCES Guest(guest_id),
  FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Department ( -- Already in 3NF as each non-key attribute is dependent on the primary key and there are no transitive dependencies.
  dept_ID INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE Employee ( -- Made hotel_id non-null to remove transitive dependency between dept_id and hotel_id.
  employee_id INT PRIMARY KEY,
  dept_id INT NOT NULL,
  employee_name VARCHAR(50),
  job_title VARCHAR(50),
  contact VARCHAR(20),
  hotel_id INT NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES Department(dept_id),
  FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

CREATE TABLE Service_Type ( -- -- Already in 3NF as each non-key attribute is dependent on the primary key and there are no transitive dependencies.
  service_type_id INT PRIMARY KEY,
  service_description VARCHAR(100) NOT NULL
  FOREIGN KEY (room_id) REFERENCES Room(room_id)
);
SELECT * FROM hotelContact;

-- Inserting dummy data into Hotel table
INSERT INTO Hotel (hotel_id, hotel_name, location) VALUES
(1, 'Hotel A', 'New York'),
(2, 'Hotel B', 'Los Angeles'),
(3, 'Hotel C', 'Chicago'),
(4, 'Hotel D', 'Miami');

-- Inserting dummy data into HotelContact table
INSERT INTO HotelContact (hotel_id, hotel_phone_number) VALUES
(1, '123-456-7890'),
(2, '987-654-3210'),
(3, '555-123-4567'),
(4, '444-555-6666');

-- Inserting dummy data into RoomType table
INSERT INTO RoomType (roomtype_id, room_type) VALUES
(1, 'Single'),
(2, 'Double'),
(3, 'Suite');

-- Inserting dummy data into RoomPrice table
INSERT INTO RoomPrice (roomtype_id, hotel_id, room_price) VALUES
(1, 1, 100.00),
(1, 2, 120.00),
(1, 3, 90.00),
(1, 4, 150.00),
(2, 1, 150.00),
(2, 2, 180.00),
(2, 3, 120.00),
(2, 4, 200.00),
(3, 1, 250.00),
(3, 2, 280.00),
(3, 3, 220.00),
(3, 4, 350.00);

-- Inserting dummy data into Room table
INSERT INTO Room (room_id, hotel_id, roomtype_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 3, 1),
(8, 3, 2),
(9, 3, 3),
(10, 4, 1),
(11, 4, 2),
(12, 4, 3);

-- Inserting dummy data into Guest table
INSERT INTO Guest (guest_id, guest_name, guest_email, guest_phone_number) VALUES
(1, 'John Doe', 'johndoe@gmail.com', '123-456-7890'),
(2, 'Jane Smith', 'janesmith@gmail.com', '555-123-4567'),
(3, 'Bob Johnson', 'bjohnson@yahoo.com', '555-555-5555'),
(4, 'Sarah Lee', 'sarahlee@hotmail.com', '444-555-6666');

-- Inserting dummy data into Booking table
INSERT INTO Booking (booking_id, guest_id, room_id, checkin_date, checkout_date, requests) VALUES
(1, 1, 1, '2023-03-12', '2023-03-15', 'No smoking room'),
(2, 2, 2, '2023-04-01', '2023-04-05', 'Late check-out'),
(3, 3, 6, '2023-05-20', '2023-05-25', ''),
(4, 4, 9, '2023-06-10', '2023-06-15', 'Room with a view');

INSERT INTO Department (dept_ID, dept_name)
VALUES
  (1, 'Front Desk'),
  (2, 'Housekeeping'),
  (3, 'Maintenance'),
  (4, 'Restaurant'),
  (5, 'Sales and Marketing');

INSERT INTO Service_Type (service_type_id, service_description)
VALUES
  (1, 'Room Cleaning'),
  (2, 'Towel and Linen Replacement'),
  (3, 'Light Fixture Replacement'),
  (4, 'Plumbing Repair'),
  (5, 'Food and Beverage Service');

SELECT * FROM Employee;
SELECT * FROM Department;
SELECT * FROM Hotel;
SELECT * FROM HotelContact;
SELECT * FROM Guest;
SELECT * FROM Booking;
SELECT * FROM Room;
SELECT * FROM roomtype;
SELECT * FROM service_type;

