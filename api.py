import datetime
from flask import Flask, jsonify, request, make_response
import mysql.connector

Mystery = Flask(__name__)


# get customers

@Mystery.route('/Customers', methods=['GET'])
def get_Customers():
    try:
        #instance_connection_name = 'inbound-byway-405423:us-central1:comp2140-group1'

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
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM OrderView")
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
def updateOStat(oID):
    try:
        con = mysql.connector.connect(user='', password ='',
                                    host = '',
                                    database = '')
        #this creates a cursor
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
            cur.execute(update_statusO, (statusO, current_time, oID))
        else:
            cur.execute(update_statusO.format(time_column=''), (statusO, None, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'statusO and time updated'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    


@Mystery.route('/cancellO/orderID', methods=['POST'])
def cancellO(oID):
    try:
        con = mysql.connector.connect(user='', password ='',
                                    host = '',
                                    database = '')
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_statusO = "UPDATE Order SET statusO = 'Cancelled', cancelTime = %s WHERE orderID = %s"

        cur.execute(update_statusO, (current_time, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been cancelled'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    

@Mystery.route('/acceptO/orderID', methods=['POST'])
def acceptO(oID):
    try:
        con = mysql.connector.connect(user='', password ='',
                                    host = '',
                                    database = '')
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_statusO = "UPDATE Order SET statusO = 'Accepted', acceptedTime = %s WHERE orderID = %s"

        cur.execute(update_statusO, (current_time, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been accepted'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    

@Mystery.route('/escalateO/orderID', methods=['POST'])
def escalateO(oID):
    try:
        con = mysql.connector.connect(user='', password ='',
                                    host = '',
                                    database = '')
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_statusO = "UPDATE Order SET statusO = 'Escalated', escalatedTime = %s WHERE orderID = %s"

        cur.execute(update_statusO, (current_time, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been escalated'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)
    


@Mystery.route('/completeO/orderID', methods=['POST'])
def completeO(oID):
    try:
        con = mysql.connector.connect(user='', password ='',
                                    host = '',
                                    database = '')
      
        cur = con.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        update_statusO = "UPDATE Order SET statusO = 'Completed', completedTime = %s WHERE orderID = %s"

        cur.execute(update_statusO, (current_time, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Order has been completed'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)



if __name__ == '__main__':
    Mystery.run(port=5000)


