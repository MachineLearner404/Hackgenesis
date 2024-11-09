from flask import Flask, request, jsonify

app = Flask(__name__)

# Example hardcoded credentials (if you need any for future implementation)
users = {
    "username": "admin",
    "password": "password123"
}

# Route for the medical form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get JSON data from the request
    data = request.get_json()

    # Validate if the necessary fields are present
    if not data or 'age' not in data or 'symptoms' not in data:
        return jsonify({"error": "Age and symptoms are required"}), 400

    age = data['age']
    symptoms = data['symptoms']  # Symptoms should be a list of selected values

    # Here you can handle the data, e.g., saving it to a database or performing some logic

    return jsonify({"message": "Form submitted successfully", "age": age, "symptoms": symptoms}), 200

# Example login route (keeping this as an example for any future needs)
@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from the request
    data = request.get_json()

    # Check if username and password are in the data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username']
    password = data['password']

    # Check if credentials match
    if username == users['username'] and password == users['password']:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
