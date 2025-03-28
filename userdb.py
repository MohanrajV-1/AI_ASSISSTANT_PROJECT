import json

# File to store user data
USER_FILE = "user_data.json"

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        print("Username already exists!")
        return False
    users[username] = password
    save_users(users)
    print("User registered successfully!")
    return True

def login_user(username, password):
    users = load_users()
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False
