
CREATE TABLE Bookings(
  BookingID INT PRIMARY KEY,
  EventSpaceID INT,
  CustomerID INT,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT,
  BookingStatus VARCHAR(20),
  FOREIGN KEY(EventSpaceID) REFERENCES EventSpaces(EventSpaceID),
  FOREIGN KEY(CustomerID) REFERENCES EventCustomer(customerID)
  );


CREATE TABLE EventSpaces(
  EventSpaceID INT PRIMARY KEY,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT
);


CREATE TABLE EventCustomer(
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255)
);
