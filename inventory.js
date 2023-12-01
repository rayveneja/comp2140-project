// Simulated inventory data retrieved from a SQL database
const inventoryData = [
    { ItemName: 'Item A', ItemID: 1, IDescription: 'Description A', DateAdded: '2023-01-01', ExpirationDate: '2023-12-31' },
    { ItemName: 'Item B', ItemID: 2, IDescription: 'Description B', DateAdded: '2023-02-01', ExpirationDate: '2023-12-31' },
];

function displayInventory() {
    // Display the inventory data
    const inventoryList = document.getElementById('inventoryList');
    inventoryList.innerHTML = ''; // Clear previous data
    inventoryData.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${item.ItemName}</strong> (ID: ${item.ItemID})<br>
                              Description: ${item.IDescription}<br>
                              Date Added: ${item.DateAdded}<br>
                              Expiration Date: ${item.ExpirationDate}
                              <button onclick="editItem(${item.ItemID})">Edit</button>`;
        inventoryList.appendChild(listItem);
    });

    // Show the inventory list section
    document.getElementById('trackingResult').innerText = 'Inventory tracking functionality will be implemented.';
    document.getElementById('inventoryList').style.display = 'block';
    document.getElementById('editOptions').style.display = 'none'; // Hide edit options when displaying inventory
}

function editItem(itemId) {
    // Find the item in the inventoryData array based on itemId
    const itemToEdit = inventoryData.find(item => item.ItemID === itemId);

    // Display the edit form with current item details
    const editForm = document.getElementById('editForm');
    editForm.innerHTML = `<h4>Edit Item</h4>
                          <label for="editedItemName">Item Name:</label>
                          <input type="text" id="editedItemName" value="${itemToEdit.ItemName}" required><br>
                          <label for="editedDescription">Description:</label>
                          <input type="text" id="editedDescription" value="${itemToEdit.IDescription}" required><br>
                          <label for="editedDateAdded">Date Added:</label>
                          <input type="date" id="editedDateAdded" value="${itemToEdit.DateAdded}" required><br>
                          <label for="editedExpirationDate">Expiration Date:</label>
                          <input type="date" id="editedExpirationDate" value="${itemToEdit.ExpirationDate}" required><br>
                          <button onclick="saveChanges(${itemId})">Save Changes</button>
                          <button onclick="cancelChanges()">Cancel Changes</button>`;

    // Hide the inventory list and display the edit form
    document.getElementById('inventoryList').style.display = 'none';
    editForm.style.display = 'block';
}

function saveChanges(itemId) {
    // Retrieve the edited values from the form
    const editedItemName = document.getElementById('editedItemName').value;
    const editedDescription = document.getElementById('editedDescription').value;
    const editedDateAdded = document.getElementById('editedDateAdded').value;
    const editedExpirationDate = document.getElementById('editedExpirationDate').value;

    // Find the item in the inventoryData array based on itemId
    const itemToEdit = inventoryData.find(item => item.ItemID === itemId);

    // Update the item details
    itemToEdit.ItemName = editedItemName;
    itemToEdit.IDescription = editedDescription;
    itemToEdit.DateAdded = editedDateAdded;
    itemToEdit.ExpirationDate = editedExpirationDate;

    // Display a message indicating that changes are saved
    document.getElementById('editingResult').innerText = 'Changes saved successfully.';

    // Re-display the inventory list
    displayInventory();
}

function cancelChanges() {
    // Hide the edit form and re-display the inventory list
    document.getElementById('editForm').style.display = 'none';
    displayInventory();
}

// Initial display of inventory
displayInventory();
