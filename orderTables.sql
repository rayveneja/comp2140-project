CREATE DATABASE MysterRestaurant;

Use MysterRestaurant;

CREATE TABLE Orders (
  orderID INT PRIMARY KEY,
  customerID INT,
  orderDetails TEXT,
  orderTotal DECIMAL(10, 2),
  orderTime TIMESTAMP,
  pickupTime TIMESTAMP,
  statusO VARCHAR(50),
  cancelledTime TIMESTAMP,
  acceptedTime TIMESTAMP,
  escalatedTime TIMESTAMP,
  staffID INT,
  FOREIGN KEY (customerID) REFERENCES Customers(customerID),
  FOREIGN KEY (staffID) REFERENCES Staff(staffID)
);

CREATE TABLE Customers (
  customerID INT PRIMARY KEY,
  customerFirstName VARCHAR(50),
  customerLastName VARCHAR(50),
  customerMiddleName VARCHAR(50).
  customerEmail VARCHAR(255),
  customerNumber VARCHAR(15)
);

CREATE TABLE Staff (
  staffID INT PRIMARY KEY,
  staffFirstName VARCHAR(50),
  staffLastName VARCHAR(50),
  staffMiddleName VARCHAR(50),
  staffEmail VARCHAR(255),
  staffNumber VARCHAR(15)
);


CREATE VIEW OrderView AS
SELECT
  o.orderID AS OrderNumber,
  CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName,
  o.orderDetails AS OrderDetails,
  o.orderTotal AS OrderTotal,
  o.pickupTime AS OrderPickupTime,
  o.statusO AS OrderStatus
FROM
  Orders o
  JOIN Customers c ON o.customerID = c.customerID;


CREATE VIEW NewOrders AS
SELECT
  o.orderID AS OrderNumber,
  CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName,
  o.orderDetails AS OrderDetails,
  o.orderTotal AS OrderTotal,
  o.pickupTime AS OrderPickupTime,
  o.statusO AS OrderStatus
FROM
  Orders o
  JOIN Customers c ON o.customerID = c.customerID
WHERE
  o.statusO = 'Pending';


CREATE VIEW AcceptedOrders AS
SELECT
  o.orderID AS OrderNumber,
  CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName,
  o.orderDetails AS OrderDetails,
  o.orderTotal AS OrderTotal,
  o.pickupTime AS OrderPickupTime,
  o.statusO AS OrderStatus,
  o.acceptedTime AS OrderAcceptedTime
FROM
  Orders o
  JOIN Customers c ON o.customerID = c.customerID
WHERE
  o.statusO = 'Accepted';


CREATE VIEW CancelledOrders AS
SELECT
  o.orderID AS OrderNumber,
  CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName,
  o.orderDetails AS OrderDetails,
  o.orderTotal AS OrderTotal,
  o.pickupTime AS OrderPickupTime,
  o.statusO AS OrderStatus,
  o.cancelTime as OrderCancelTime
FROM
  Orders o
  JOIN Customers c ON o.customerID = c.customerID
WHERE
  o.statusO = 'Cancelled';


CREATE VIEW EscalatedOrders AS
SELECT
  o.orderID AS OrderNumber,
  CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName,
  o.orderDetails AS OrderDetails,
  o.orderTotal AS OrderTotal,
  o.pickupTime AS OrderPickupTime,
  o.statusO AS OrderStatus,
  o.escalatedTime AS OrderEscalatedTime
FROM
  Orders o
  JOIN Customers c ON o.customerID = c.customerID
WHERE
  o.statusO = 'Escalated';

