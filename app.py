import datetime
from flask import Flask, jsonify, request, make_response
import mysql.connector
from flask_cors import CORS

Mystery = Flask(__name__)
CORS(Mystery)

# get all bookings

@Mystery.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT EventSpaces.EventName, EventCustomer.CustomerName, Bookings.EventDateTime, Bookings.EventDuration, Bookings.BookingStatus FROM Bookings JOIN EventSpaces ON Bookings.EventSpaceID = EventSpaces.EventSpaceID JOIN EventCustomer ON Bookings.CustomerID = EventCustomer.CustomerID;")
        booking_list = []
        for row in cursor.fetchall():
            booking = {
                'EventName': row[0],
                'CustomerName': row[1],
                'EventDateTime': row[2],
                'EventDuration': row[3],
                'BookingStatus': row[4]
            }
            booking_list.append(booking)
        cursor.close()
        con.close()
        return make_response(jsonify(booking_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving this view'}), 500)



# get bookings with a status available
@Mystery.route('/available-bookings', methods=['GET'])
def get_available_bookings():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT EventSpaces.EventName, EventCustomer.CustomerName, Bookings.EventDateTime, Bookings.EventDuration FROM Bookings JOIN EventSpaces ON Bookings.EventSpaceID = 
        EventSpaces.EventSpaceID JOIN EventCustomer ON Bookings.CustomerID = EventCustomer.CustomerID WHERE Bookings.BookingStatus = 'available';")
        available_booking_list = []
        for row in cursor.fetchall():
            booking = {
                'EventName': row[0],
                'CustomerName': row[1],
                'EventDateTime': row[2],
                'EventDuration': row[3],
            }
            available_booking_list.append(booking)
        cursor.close()
        con.close()
        return make_response(jsonify(available_booking_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving available bookings'}), 500)


# get bookings by status
@Mystery.route('/bookings-by-status/<status>', methods=['GET'])
def get_bookings_by_status(status):
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()

        
        if status.lower() not in ['approve', 'reject']:
            return make_response(jsonify({'error': 'Invalid status provided'}), 400)

        cursor.execute(f"SELECT EventSpaces.EventName, EventCustomer.CustomerName, Bookings.EventDateTime, Bookings.EventDuration FROM Bookings JOIN EventSpaces ON Bookings.EventSpaceID = 
        EventSpaces.EventSpaceID JOIN EventCustomer ON Bookings.CustomerID = EventCustomer.CustomerID WHERE Bookings.BookingStatus = %s;", (status,))
        bookings_by_status_list = []

        for row in cursor.fetchall():
            booking = {
                'EventName': row[0],
                'CustomerName': row[1],
                'EventDateTime': row[2],
                'EventDuration': row[3],
            }
            bookings_by_status_list.append(booking)

        cursor.close()
        con.close()
        return make_response(jsonify(bookings_by_status_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving bookings by status'}), 500)





if __name__ == '__main__':
    Mystery.run(port=5000)


