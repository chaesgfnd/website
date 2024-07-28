from flask import Flask, jsonify, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Route to return JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(sample_data)

# Route to handle a POST request
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    response = {
        'message': 'Data received',
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
