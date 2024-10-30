from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

class SecureStorage:
    def __init__(self, encryption_manager):
        self.encryption_manager = encryption_manager
        self.storage = {}

    def store_data(self, key, data):
        encrypted_data = self.encryption_manager.encrypt(data)
        self.storage[key] = encrypted_data

    def retrieve_data(self, key):
        encrypted_data = self.storage.get(key, None)
        if encrypted_data:
            return self.encryption_manager.decrypt(encrypted_data)
        return None
