import datetime
from flask import Flask, jsonify, request, make_response
import mysql.connector
from flask_cors import CORS

Mystery = Flask(__name__)
CORS(Mystery)

# get customers

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



if __name__ == '__main__':
    Mystery.run(port=5000)


