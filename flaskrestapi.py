from flask import Flask, request
import requests

app = Flask(__name__)

# Some sample data
data = [
    {'id': 1, 'name': 'Ali'},
    {'id': 2, 'name': 'Veli'},
    {'id': 3, 'name': 'Ayse'},
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return {'users': data}

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in data:
        if user['id'] == user_id:
            return user
    return None

@app.route('/api/users', methods=['POST'])
def users():
    if request.method == 'POST':
        # Get the data from the POST request
        user = request.get_json()
        # Add the new user to the list
        data.append(user)
        return {'status': 'success'}

if __name__ == '__main__':
    app.run()

	

# Get all users
response = requests.get('http://localhost:5000/api/users')
print(response.json())

# Get user with ID 2
response = requests.get('http://localhost:5000/api/users/2')
print(response.json())

# post
response = requests.post('http://localhost:5000/api/users', json={'id': 5, 'name': 'Elif'})
print(response.json())

#print all 
print(requests.get('http://localhost:5000/api/users').json())
