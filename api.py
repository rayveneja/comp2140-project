from datetime import datetime
from flask import Flask, jsonify, request, make_response
import mysql.connector
from flask_cors import CORS

Mystery = Flask(__name__)
CORS(Mystery)

# get customers

@Mystery.route('/Customers', methods=['GET'])
def get_Customers():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Customers")
        customer_list = []
        for row in cursor.fetchall():
            customer = {
                'customerID': row[0],
                'customerFirstName': row[1],
                'customerLastName': row[2],
                'customerMiddleName': row[3]
            }
            customer_list.append(customer)
        cursor.close()
        con.close()
        return make_response(jsonify(customer_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving this view'}), 500)


  # get orders for display view
@Mystery.route('/ordersView', methods=['GET'])
def get_orderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root', host='localhost', database='mysteryRest')
        cursor = con.cursor()
        cursor.execute(f"SELECT o.orderID AS OrderNumber, CONCAT(c.customerFirstName, ' ', c.customerLastName) AS CustomerFullName, o.orderDetails AS OrderDetails, o.orderTotal AS OrderTotal,o.pickupTime AS OrderPickupTime, o.statusO AS OrderStatus FROM Orders o JOIN Customers c ON o.customerID = c.customerID;")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus in cursor:
            order = {
                'OrderNumber': OrderNumber,
                'CustomerFullName': CustomerFullName,
                'OrderDetails': OrderDetails,
                'OrderTotal': OrderTotal,
                'OrderPickupTime': OrderPickupTime,
                'OrderStatus': OrderStatus
            }
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving this view'}), 500)
    
@Mystery.route('/ordersView/<int:orderID>', methods=['GET'])
def get_orderViewbyID(orderID):
    try:
        # connect to database
        con = mysql.connector.connect(user='root', host='localhost', database='mysteryRest')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM OrderView WHERE orderView.OrderNumber={orderID}")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus in cursor:
            order = {
                'Order Number': OrderNumber,
                'Customer Name': CustomerFullName,
                'Details': OrderDetails,
                'Total': OrderTotal,
                'PickupTime': OrderPickupTime,
                'Status': OrderStatus
            }
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving this view'}), 500)


    
    
@Mystery.route('/NewOrdersView', methods=['GET'])
def get_NeworderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM NewOrders")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus in cursor:
            order = {}
            order['OrderNumber'] = OrderNumber
            order['CustomerFullName'] = CustomerFullName
            order['OrderDetails'] = OrderDetails
            order['OrderTotal'] = OrderTotal
            order['OrderPickupTime'] = OrderPickupTime
            order['OrderStatus'] = OrderStatus
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)
    
    
@Mystery.route('/acceptedOrdersView', methods=['GET'])
def get_acceptedorderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM AcceptedOrders")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus, OrderAcceptedTime in cursor:
            order = {}
            order['OrderNumber'] = OrderNumber
            order['CustomerFullName'] = CustomerFullName
            order['OrderDetails'] = OrderDetails
            order['OrderTotal'] = OrderTotal
            order['OrderPickupTime'] = OrderPickupTime
            order['OrderStatus'] = OrderStatus
            order['OrderAcceptedTime'] = OrderAcceptedTime
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)


@Mystery.route('/cancelledOrdersView', methods=['GET'])
def get_cancelledorderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM CancelledOrders")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus, OrderCancelTime in cursor:
            order = {}
            order['OrderNumber'] = OrderNumber
            order['CustomerFullName'] = CustomerFullName
            order['OrderDetails'] = OrderDetails
            order['OrderTotal'] = OrderTotal
            order['OrderPickupTime'] = OrderPickupTime
            order['OrderStatus'] = OrderStatus
            order['OrderCancelTime'] = OrderCancelTime
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)


@Mystery.route('/escalatedOrdersView', methods=['GET'])
def get_escalatedorderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM EscalatedOrders")
        orderView_list = []
        for OrderNumber, CustomerFullName, OrderDetails, OrderTotal, OrderPickupTime, OrderStatus, OrderEscalatedTime in cursor:
            order = {}
            order['OrderNumber'] = OrderNumber
            order['CustomerFullName'] = CustomerFullName
            order['OrderDetails'] = OrderDetails
            order['OrderTotal'] = OrderTotal
            order['OrderPickupTime'] = OrderPickupTime
            order['OrderStatus'] = OrderStatus
            order['OrderEscalatedTime'] = OrderEscalatedTime
            orderView_list.append(order)
        cursor.close()
        con.close()
        return make_response(jsonify(orderView_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)
   
    
    
@Mystery.route('/updateOStat/orderID', methods=['POST'])
def updateOStat(orderID):
    try:
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cur = con.cursor()
        content = request.json
        statusO = content['statusO']

        update_statusO = "UPDATE Order SET statusO = %s, {time_column} = %s WHERE orderID = %s"

        if statusO == 'Accepted':
            time_column = 'acceptedTime'
        elif statusO == 'Completed':
            time_column = 'completedTime'
        elif statusO == 'Cancelled':
            time_column = 'cancelTime'
        elif statusO == 'Escalted':
            time_column = 'escalatedTime'
        else:
            time_column = None
        
        if time_column:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            update_statusO = update_statusO.format(time_column=time_column)
            cur.execute(update_statusO, (statusO, current_time, orderID))
        else:
            cur.execute(update_statusO.format(time_column=''), (statusO, None, orderID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'statusO and time updated'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    


@Mystery.route('/cancellO/<int:orderID>', methods=['POST'])
def cancellO(orderID):
    try:
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_statusO = """
            UPDATE Orders 
            SET statusO = 'Cancelled', 
                cancelledTime = %s 
            WHERE orderID = %s
        """

        cur.execute(update_statusO, (current_time, orderID))


        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been cancelled'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    
    

@Mystery.route('/acceptO/<int:orderID>', methods=['POST'])
def acceptO(orderID):
    try:
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_statusO = """
            UPDATE Orders 
            SET statusO = 'Accepted', 
                acceptedTime = %s 
            WHERE orderID = %s
        """

        cur.execute(update_statusO, (current_time, orderID))


        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been accepted'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    

@Mystery.route('/escalateO/<int:orderID>', methods=['POST'])
def escalateO(orderID):
    try:
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_statusO = """
            UPDATE Orders 
            SET statusO = 'Escalated', 
                escalatedTime = %s 
            WHERE orderID = %s
        """

        cur.execute(update_statusO, (current_time, orderID))


        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been escalated'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    


@Mystery.route('/completeO/<int:orderID>', methods=['POST'])
def completeO(orderID):
    try:
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_statusO = """
            UPDATE Orders 
            SET statusO = 'Completed', 
                completedTime = %s 
            WHERE orderID = %s
        """

        cur.execute(update_statusO, (current_time, orderID))


        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been completed'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    

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
        cursor.execute(f"SELECT EventSpaces.EventName, EventCustomer.CustomerName, Bookings.EventDateTime, Bookings.EventDuration FROM Bookings JOIN EventSpaces ON Bookings.EventSpaceID = EventSpaces.EventSpaceID JOIN EventCustomer ON Bookings.CustomerID = EventCustomer.CustomerID WHERE Bookings.BookingStatus = 'available';")
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

    
    


if __name__ == '__main__':
    Mystery.run(port=5000)


