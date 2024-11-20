from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Facility 360!"

@app.route('/work-order', methods=['POST'])
def work_order():
    data = request.get_json()  # Get JSON data from the request body
    if not data or 'description' not in data:
        return jsonify({"error": "Please provide a work order description."}), 400
    
    description = data['description']
    return jsonify({"message": "Work order received!", "description": description})

if __name__ == "__main__":
    app.run(debug=True)
