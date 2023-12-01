// Define acceptOrder globally
function acceptOrder(orderId) {
    fetch(`http://localhost:5000/acceptO/${orderId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Status: 'Accepted' }), // Adjust payload as needed
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(updatedOrder => {
            // Display a message at the bottom of the popup
            const messageContainer = document.getElementById('popupMessage');
            messageContainer.textContent = 'Order Accepted.';

            // Fetch and display updated order details
            fetchOrderDetailsById(updatedOrder);
        })
        .catch(error => {
            console.error('Error accepting order:', error);
        });
}

// Define acceptOrder globally
function cancelOrder(orderId) {
    fetch(`http://localhost:5000/cancellO/${orderId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Status: 'Cancelled' }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(updatedOrder => {
            // Display a message at the bottom of the popup
            const messageContainer = document.getElementById('popupMessage');
            messageContainer.textContent = 'Order Cancel.';

            // Fetch and display updated order details
            fetchOrderDetailsById(updatedOrder);
        })
        .catch(error => {
            console.error('Error accepting order:', error);
        });
}


function escalateOrder(orderId) {
    fetch(`http://localhost:5000/escalateO/${orderId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Status: 'Escalated' }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(updatedOrder => {
            // Display a message at the bottom of the popup
            const messageContainer = document.getElementById('popupMessage');
            messageContainer.textContent = 'Order Escalated.';

            // Fetch and display updated order details
            fetchOrderDetailsById(updatedOrder);
        })
        .catch(error => {
            console.error('Error accepting order:', error);
        });
}

function completeOrder(orderId) {
    fetch(`http://localhost:5000/escalateO/${orderId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Status: 'Completed' }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(updatedOrder => {
            // Display a message at the bottom of the popup
            const messageContainer = document.getElementById('popupMessage');
            messageContainer.textContent = 'Order Completed';

            // Fetch and display updated order details
            fetchOrderDetailsById(updatedOrder);
        })
        .catch(error => {
            console.error('Error accepting order:', error);
        });
}



document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch order details and update the table
    function fetchOrderDetails() {
        fetch('http://localhost:5000/ordersView')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // update order details table with the data
                const orderTableBody = document.getElementById('orderDetails');

                orderTableBody.innerHTML = '';

                // add the data
                data.forEach(order => {
                    const row = orderTableBody.insertRow();
                    row.classList.add('order');
                    row.setAttribute('data-order-id', order.OrderNumber);
                    row.insertCell(0).textContent = order.OrderNumber;
                    row.insertCell(1).textContent = order.CustomerFullName;
                    row.insertCell(2).textContent = order.OrderDetails;
                    row.insertCell(3).textContent = order.OrderTotal;
                    row.insertCell(4).textContent = order.OrderPickupTime;
                    row.insertCell(5).textContent = order.OrderStatus;

                    // Add an attribute to store order data
                    row.setAttribute('data-order', JSON.stringify(order));

                    // Attach click event listener to the row
                    row.addEventListener('click', function () {
                        fetchOrderDetailsById(order);
                    });
                });
            })
            .catch(error => {
                console.error('Error fetching order details:', error);
            });
    }

    // get order details by ID
    function fetchOrderDetailsById(order) {
        const orderId = order.OrderNumber;

        fetch(`http://localhost:5000/ordersView/${orderId}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Display the order details in the modal
                const orderDetailsModal = document.getElementById('orderDetailsModal');
                const orderDetailsTable = document.getElementById('orderDetailsTable');

                // Clear previous content
                orderDetailsTable.innerHTML = '';

                // Append new content
                data.forEach(detail => {
                    // Create a list item for each detail
                    for (const key in detail) {
                        if (detail.hasOwnProperty(key)) {
                            const listItem = document.createElement('li');
                            listItem.innerHTML = `<strong>${key}:</strong> ${detail[key]}`;
                            orderDetailsTable.appendChild(listItem);
                        }
                    }
                });

                // Add action buttons to the modal
                const actionButtons = document.getElementById('actionButtons');
                actionButtons.innerHTML = `
                    <button id="acceptButton">Accept</button>
                    <button id="cancelButton">Cancel</button>
                    <button id="completeButton">Complete</button>
                    <button id="escalateButton">Escalate</button>
                `;

                // Attach click event listeners to the buttons
                document.getElementById('acceptButton').addEventListener('click', function () {
                    acceptOrder(orderId);
                });

                document.getElementById('cancelButton').addEventListener('click', function () {
                    cancelOrder(orderId);
                });

                document.getElementById('completeButton').addEventListener('click', function () {
                    completeOrder(orderId);
                });

                document.getElementById('escalateButton').addEventListener('click', function () {
                    escalateOrder(orderId);
                });

                // display modal
                orderDetailsModal.style.display = 'block';
            })
            .catch(error => {
                console.error('Error fetching order details by ID:', error);
            });
    }

    const closeIcon = document.querySelector('.close');
    closeIcon.addEventListener('click', function () {
        closeOrderDetailsModal();
    });

    // Define closeOrderDetailsModal function
    function closeOrderDetailsModal() {
        const orderDetailsModal = document.getElementById('orderDetailsModal');

        // Close the popup
        orderDetailsModal.style.display = 'none';

        // Refresh the page
        location.reload();
    }

    // Fetch initial order details
    fetchOrderDetails();
});
