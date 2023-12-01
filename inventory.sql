CREATE TABLE Items(
  ItemID INT PRIMARY KEY,
  InventoryItemsID INT,
  ItemName VARCHAR(255),
  IDescription VARCHAR(255),
  DateAdded DATETIME,
  ExpirationDate DATETIME,
  FOREIGN KEY(InventoryItemsID) REFERENCES InventoryItems(InventoryItemsID)
);
