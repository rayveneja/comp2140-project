// Sample bookings array
let bookings = [];

function submitBooking() {
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    if (name && date && time) {
        const booking = { name, date, time };
        bookings.push(booking);

        // Update the bookings table
        updateBookingTable();

        // Clear the form fields
        document.getElementById('name').value = '';
        document.getElementById('date').value = '';
        document.getElementById('time').value = '';

        // You can add logic to send confirmation emails here (requires server-side implementation)
    } else {
        alert('Please fill in all fields');
    }
}

function updateBookingTable() {
    const bookingList = document.getElementById('booking-list');
    // Clear existing rows
    bookingList.innerHTML = '';

    // Add new rows based on the bookings array
    bookings.forEach(booking => {
        const row = bookingList.insertRow();
        const nameCell = row.insertCell(0);
        const dateCell = row.insertCell(1);
        const timeCell = row.insertCell(2);

        nameCell.textContent = booking.name;
        dateCell.textContent = booking.date;
        timeCell.textContent = booking.time;
    });
}
