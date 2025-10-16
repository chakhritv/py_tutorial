from flask import Flask, request, jsonify

app = Flask(__name__)
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    item = data.get('item')
    if item:
        items.append(item)
        return jsonify({'message': 'Item added', 'item': item}), 201
    return jsonify({'error': 'No item provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
