
CREATE TABLE Bookings(
  BookingID INT PRIMARY KEY,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255),
  Status VARCHAR(20)
  );


CREATE TABLE EventSpaces(
  EventSpaceID INT PRIMARY KEY,
  EventName VARCHAR(255),
  EventDateTime DATETIME,
  EventDuration INT,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255),
  Status VARCHAR(20)
);


CREATE TABLE BookingRequests(
  RequestID INT PRIMARY KEY,
  EventName VARCHAR(255),
  RequestedDateTime DATETIME,
  RequestedDuration INT,
  CustomerName VARCHAR(255),
  CustomerPhone VARCHAR(20),
  CustomerEmail VARCHAR(255),
  Status VARCHAR(20)

);