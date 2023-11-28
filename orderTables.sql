CREATE DATABASE MysterRestaurant;

Use MysterRestaurant;

CREATE TABLE Orders (
  orderID INT PRIMARY KEY,
  customerID INT,
  orderDetails TEXT,
  orderTotal DECIMAL(10, 2),
  orderTime TIMESTAMP,
  pickupTime TIMESTAMP,
  isCancelled BOOLEAN,
  isCompleted BOOLEAN,
  isAcknowledged BOOLEAN,
  orderClosedTime TIMESTAMP,
  orderAcknowledgedTime TIMESTAMP,
  staffID INT,
  FOREIGN KEY (customerID) REFERENCES Customers(customerID),
  FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Customers (
  customerID INT PRIMARY KEY,
  customerFirstName VARCHAR(50),
  customerLastName VARCHAR(50),
  customerMiddleName VARCHAR(50)
);

CREATE TABLE Staff (
  staffID INT PRIMARY KEY,
  staffFirstName VARCHAR(50),
  staffLastName VARCHAR(50),
  staffMiddleName VARCHAR(50)
);

CREATE TABLE OrderAlerts (
  alertID INT PRIMARY KEY,
  orderID INT,
  alertTime TIMESTAMP,
  isHandled BOOLEAN,
  FOREIGN KEY (orderID) REFERENCES Orders(orderID)
);