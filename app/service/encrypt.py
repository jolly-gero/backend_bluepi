from cryptography.fernet import Fernet

class GameKey:

    def generate_key(self):
        key = Fernet.generate_key()
        return key

    def encrypts(self, message, key):
        encoded_message = message.encode("utf-8")
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)

        return encrypted_message

    def decrypted(self, encrypted_message, key):
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        decoded_message = decrypted_message.decode("utf-8")

        return decoded_message
