from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return jsonify(message="Login successful")
    else:
        return jsonify(message="Invalid credentials")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)