const inventoryData = [
    { ItemName: 'Item A', ItemID: 1, IDescription: 'Description A', DateAdded: '2023-01-01', ExpirationDate: '2023-12-31' },
    { ItemName: 'Item B', ItemID: 2, IDescription: 'Description B', DateAdded: '2023-02-01', ExpirationDate: '2023-12-31' },
];

let currentInventory = [...inventoryData];

function searchItem() {
    const searchValue = document.getElementById('searchItem').value.toLowerCase();
    currentInventory = inventoryData.filter(item =>
        item.ItemName.toLowerCase().includes(searchValue)
    );

    displayInventory();
}

function toggleAddForm() {
    const inventoryItems = document.getElementById('inventoryItems');
    const addForm = document.getElementById('addForm');

    if (inventoryItems.style.display === 'block') {
        inventoryItems.style.display = 'none';
        addForm.style.display = 'block';
    } else {
        inventoryItems.style.display = 'block';
        addForm.style.display = 'none';
    }
}

function addItem() {
    const newItemName = document.getElementById('newItemName').value;
    const newDescription = document.getElementById('newDescription').value;
    const newDateAdded = document.getElementById('newDateAdded').value;
    const newExpirationDate = document.getElementById('newExpirationDate').value;

    const newItem = {
        ItemName: newItemName,
        ItemID: currentInventory.length + 1,
        IDescription: newDescription,
        DateAdded: newDateAdded,
        ExpirationDate: newExpirationDate,
    };

    currentInventory.push(newItem);
    displayInventory();
}

function cancelAdd() {
    document.getElementById('newItemName').value = '';
    document.getElementById('newDescription').value = '';
    document.getElementById('newDateAdded').value = '';
    document.getElementById('newExpirationDate').value = '';

    toggleAddForm();
    displayInventory();
}

function deleteItem(itemId) {
    const confirmation = confirm('Are you sure you want to delete this item?');
    if (confirmation) {
        const indexToDelete = currentInventory.findIndex(item => item.ItemID === itemId);

        if (indexToDelete !== -1) {
            currentInventory.splice(indexToDelete, 1);
            document.getElementById('editingResult').innerText = 'Item deleted successfully.';
            displayInventory();
        }
    }
}

function displayInventory() {
    const inventoryList = document.getElementById('itemsList');
    inventoryList.innerHTML = '';

    currentInventory.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>${item.ItemName}</strong> (ID: ${item.ItemID})<br>
                              Description: ${item.IDescription}<br>
                              Date Added: ${item.DateAdded}<br>
                              Expiration Date: ${item.ExpirationDate}
                              <button onclick="editItem(${item.ItemID})">Edit</button>
                              <button onclick="deleteItem(${item.ItemID})">Delete</button>`;
        inventoryList.appendChild(listItem);
    });

    document.getElementById('inventoryItems').style.display = 'block';
    document.getElementById('addForm').style.display = 'none';
}

function editItem(itemId) {
    const itemToEdit = currentInventory.find(item => item.ItemID === itemId);

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

    document.getElementById('inventoryItems').style.display = 'none';
    document.getElementById('editForm').style.display = 'block';
}

function saveChanges(itemId) {
    const editedItemName = document.getElementById('editedItemName').value;
    const editedDescription = document.getElementById('editedDescription').value;
    const editedDateAdded = document.getElementById('editedDateAdded').value;
    const editedExpirationDate = document.getElementById('editedExpirationDate').value;

    const itemToEdit = currentInventory.find(item => item.ItemID === itemId);

    itemToEdit.ItemName = editedItemName;
    itemToEdit.IDescription = editedDescription;
    itemToEdit.DateAdded = editedDateAdded;
    itemToEdit.ExpirationDate = editedExpirationDate;

    const confirmation = confirm('Changes Saved Successfully!');

    displayInventory();

    document.getElementById('editForm').style.display = 'none';
    document.getElementById('inventoryItems').style.display = 'block';
}

function cancelChanges() {
    document.getElementById('editForm').style.display = 'none';
    displayInventory();
}

// Initial display of inventory
displayInventory();
