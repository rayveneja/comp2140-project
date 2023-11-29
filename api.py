import datetime
from flask import Flask, jsonify, request, make_response
import mysql.connector

Mystery = Flask(__name__)

# get customers

@Mystery.route('/Customers', methods=['GET'])
def get_Customers():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='',
                                       database=''
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Customers")
        customer_list = []
        for customerID, customerFirstName, customerLastName, customerMiddleName in cursor:
            customer = {}
            customer['customerID'] = customerID
            customer['customerFirstName'] = customerFirstName
            customer['customerLastName'] = customerLastName
            customer['customerMiddleName'] = customerMiddleName
            customer_list.append(customer)
        cursor.close()
        con.close()
        return make_response(jsonify(customer_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retreiving this view'}), 500)
    

  # get orders for display view

@Mystery.route('/ordersView', methods=['GET'])
def get_orderView():
    try:
        # connect to database
        con = mysql.connector.connect(user='root',
                                       host='',
                                       database=''
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM OrderView")
        orderView_list = []
        for orderDetails, orderTotal, orderTime, customerName in cursor:
            order = {}
            order['customerID'] = orderDetails
            order['customerFirstName'] = orderTotal
            order['customerLastName'] = orderTime
            order['customerMiddleName'] = customerName
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
        status = content['Status']

        update_status = "UPDATE Order SET status = %s, {time_column} = %s WHERE orderID = %s"

        if status == 'Accepted':
            time_column = 'acceptedTime'
        elif status == 'Completed':
            time_column = 'completedTime'
        elif status == 'Cancelled':
            time_column = 'cancelTime'
        else:
            time_column = None
        
        if time_column:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            update_status = update_status.format(time_column=time_column)
            cur.execute(update_status, (status, current_time, oID))
        else:
            cur.execute(update_status.format(time_column=''), (status, None, oID))

        con.commit()
        cur.close()
        con.close()
        return make_response({'message': 'Status and time updated'}, 200)

    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)

    



if __name__ == '__main__':
    Mystery.run(port=5000)


