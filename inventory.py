from flask import Flask, jsonify, request, make_response, render_template
import random
import datetime

app = Flask(__name__)

# Simulated inventory data retrieved from a SQL database
inventory_data = [
    {'ItemID': 1, 'ItemName': 'Item A', 'IDescription': 'Description A', 'DateAdded': '2023-01-01', 'ExpirationDate': '2023-12-31'},
    {'ItemID': 2, 'ItemName': 'Item B', 'IDescription': 'Description B', 'DateAdded': '2023-02-01', 'ExpirationDate': '2023-12-31'},
]

# Simulated audit trail data
audit_trail_data = [
    {'ItemID': 1, 'Changes': 'Added new item'},
    {'ItemID': 2, 'Changes': 'Updated quantity'},
]

# Route for rendering the inventory page
@app.route('/inventory', methods=['GET'])
def inventory():
    return render_template('inventory.html')

# Route for handling inventory-related actions
@app.route('/inventory/actions', methods=['POST'])
def inventory_actions():
    try:
        action = request.form.get('action')

        if action == 'searchItem':
            search_item_value = request.form.get('searchItemValue')
            # Simulated data for search results
            search_results = random.sample(inventory_data, k=min(len(inventory_data), 3))
            return jsonify({'searchResults': search_results})

        elif action == 'editInventory':
            item_id = int(request.form.get('itemID'))
            # Find the item in the inventory data based on item ID
            selected_item = next((item for item in inventory_data if item['ItemID'] == item_id), None)
            return jsonify({'selectedItem': selected_item})

        elif action == 'saveChanges':
            # Perform any necessary actions for saving changes
            return jsonify({'result': 'Changes saved successfully.'})

        elif action == 'cancelChanges':
            # Perform any necessary actions for canceling changes
            return jsonify({'result': 'Changes canceled.'})

        elif action == 'getAuditTrail':
            item_id = int(request.form.get('itemID'))
            # Simulated data for audit trail
            item_audit_trail = [audit for audit in audit_trail_data if audit['ItemID'] == item_id]
            return jsonify({'auditTrail': item_audit_trail})

        else:
            return jsonify({'error': 'Invalid action'})

    except Exception as e:
        print(e)
        return make_response(jsonify({'error': 'An error occurred while processing the request'}), 500)

if __name__ == '__main__':
    app.run(port=5000)

