import bcrypt

# Hash the password before storing
password = "123456"
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

user_data = {
    "username": "john_doe",
    "password": hashed_password
}

def authenticate(username, password):
    if user_data["username"] == username and bcrypt.checkpw(password.encode(), user_data["password"]):
        return "Login successful"
    return "Invalid credentials"

print(authenticate("john_doe", "123456"))
