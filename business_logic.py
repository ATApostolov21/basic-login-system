import json

def create_user(username, password):
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        users = {}

    # Create a dictionary with the 'password' key
    users[username] = {'password': password}

    with open('users.json', 'w') as f:
        json.dump(users, f, indent=2)

# Your other functions remain unchanged
def authenticate_user(username, password):
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)

        # Check if the user exists and the password is correct
        if username in users and 'password' in users[username] and users[username]['password'] == password:
            return True
        else:
            return False
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return False

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
        return users
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return {}

def save_user(username, password):
    users = load_users()
    users[username] = {'password': password}

    with open('users.json', 'w') as file:
        json.dump(users, file, indent=2)
