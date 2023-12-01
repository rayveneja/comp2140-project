
CREATE TABLE Bookings(
  BookingID INT PRIMARY KEY,
  EventSpaceID INT,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255),
  BookingStatus VARCHAR(20)
  );


CREATE TABLE EventSpaces(
  EventSpaceID INT PRIMARY KEY,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT,
);


CREATE TABLE EventCustomer(
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255),
  Status VARCHAR(20)

);






