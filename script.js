document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch booking details and update the table
    function fetchBookingDetails() {
        fetch('http://localhost:5000/bookings')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // update booking details table with the data
                const bookingListSection = document.getElementById('booking-list');

                // Clear previous content
                bookingListSection.innerHTML = '';

                // Add the data
                data.forEach(booking => {
                    const bookingInfo = document.createElement('p');
                    bookingInfo.textContent = `Event: ${booking.EventName}, Customer: ${booking.CustomerName}, 
                    Date: ${booking.EventDateTime}, Duration: ${booking.EventDuration}, Status: 
                    ${booking.BookingStatus}`;
                    bookingListSection.appendChild(bookingInfo);
                });
            })
            .catch(error => {
                console.error('Error fetching booking details:', error);
            });
    }

    // Fetch booking details on page load
    fetchBookingDetails();
});
