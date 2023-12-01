-- SQL script for creating a test inventory table
CREATE TABLE Inventory (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(255),
    IDescription VARCHAR(255),
    DateAdded DATE,
    ExpirationDate DATE
);

-- Inserting test data into the inventory table
INSERT INTO Inventory (ItemID, ItemName, IDescription, DateAdded, ExpirationDate) VALUES
(1, 'Item A', 'Description A', '2023-01-01', '2023-12-31'),
(2, 'Item B', 'Description B', '2023-02-01', '2023-12-31');
