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

                //add the data
                data.forEach(order => {
                    const row = orderTableBody.insertRow();
                    row.classList.add('order');
                    row.setAttribute('data-order-id', order.OrderNumber);
                    row.onclick = function () {
                        fetchOrderDetailsById(order.OrderNumber);
                    };

                    row.insertCell(0).textContent = order.OrderNumber;
                    row.insertCell(1).textContent = order.CustomerFullName;
                    row.insertCell(2).textContent = order.OrderDetails;
                    row.insertCell(3).textContent = order.OrderTotal;
                    row.insertCell(4).textContent = order.OrderPickupTime;
                    row.insertCell(5).textContent = order.OrderStatus;
                });
            })
            .catch(error => {
                console.error('Error fetching order details:', error);
            });
    }

    // get order details by ID
    function fetchOrderDetailsById(orderId) {
        
        orderId = parseInt(orderId, 10);
    
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
    
                // display modal
                orderDetailsModal.style.display = 'block';


            })
            .catch(error => {
                console.error('Error fetching order details by ID:', error);
            });
    }

    fetchOrderDetails();
});
