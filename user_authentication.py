class UserAuthentication:
    def __init__(self):
        self.credentials = {}  # Store usernames and hashed passwords

    def register_user(self, username, password):
        # Logic to hash the password and store it
        self.credentials[username] = password  # Replace with hashed password

    def authenticate_user(self, username, password):
        # Check if the username exists and the password matches
        stored_password = self.credentials.get(username)
        return stored_password == password  # Replace with hashed check
