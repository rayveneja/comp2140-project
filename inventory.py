import datetime
from flask import Flask, jsonify, request, make_response, render_template
import mysql.connector
from flask_cors import CORS

Mystery = Flask(__name__)
CORS(Mystery)


# Route for rendering the inventory page
@Mystery.route('/inventory', methods=['GET'])
def inventory():
    try:
        # Connect to database
        con = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysteryRest'
                                       )
        cursor = con.cursor()
        cursor.execute(f"SELECT Item.ItemName, Item.ItemID, Item.IDescription, Item.DateAdded, Item.ExpirationDate FROM Items.InventoryItemsID = Items.InventoryItemsID")
        item_list = []
        for row in cursor.fetchall():
            item = {
                'ItemName': row[0],
                'ItemID': row[1],
                'IDescription': row[2],
                'DateAdded': row[3],
                'ExpirationDate': row[4]
            }
            item_list.append(item)
        cursor.close()
        con.close()
        return make_response(jsonify(item_list), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while retrieving this view'}), 500)
    
# Route for handling inventory-related actions (e.g., search, track, edit)
@Mystery.route('/inventory/actions', methods=['POST'])
def inventory_actions():
    try:
        action = request.form.get('action')

        if action == 'searchItem':
            search_item_value = request.form.get('searchItemValue')
            # Perform any necessary actions for searching items (e.g., query the database)
            return jsonify({'result': f'Searching for item: {search_item_value}'})

        elif action == 'trackInventory':
            # Simulated data retrieved from a SQL database
            audit_trail_data = [
                {'item': 'Item A', 'changes': 'Added new item'},
                {'item': 'Item B', 'changes': 'Updated quantity'},
            ]
            return jsonify({'auditTrailData': audit_trail_data})

        elif action == 'editInventory':
            # Perform any necessary actions for editing inventory
            return jsonify({'result': 'Inventory editing functionality will be implemented.'})

        elif action == 'saveChanges':
            # Perform any necessary actions for saving changes
            return jsonify({'result': 'Changes saved successfully.'})

        elif action == 'cancelChanges':
            # Perform any necessary actions for canceling changes
            return jsonify({'result': 'Changes canceled.'})

        else:
            return jsonify({'error': 'Invalid action'})

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while processing the request'}), 500)

if __name__ == '__main__':
    Mystery.run(port=5000)
