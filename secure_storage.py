class SecureStorage:
    def __init__(self, encryption_manager):
        self.encryption_manager = encryption_manager
        self.storage = {}  # Simulating storage

    def store_data(self, key, data):
        encrypted_data = self.encryption_manager.encrypt(data)
        self.storage[key] = encrypted_data

    def retrieve_data(self, key):
        encrypted_data = self.storage.get(key)
        if encrypted_data:
            return self.encryption_manager.decrypt(encrypted_data)
        return None


class EncryptionManager:
    pass