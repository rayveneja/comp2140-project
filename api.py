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
    



if __name__ == '__main__':
    Mystery.run(port=5000)


