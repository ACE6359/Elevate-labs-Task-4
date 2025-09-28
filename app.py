from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Something went wrong"}), 500

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

# POST - Add new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify(users[user_id]), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify(users[user_id]), 200

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200


if __name__ == '__main__':
    app.run(debug=True)

