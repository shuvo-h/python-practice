import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(key, text):
    # Ensure the key is 16, 24, or 32 bytes long
    key = key.ljust(32)[:32].encode()  # Pad or truncate key to 32 bytes
    cipher = AES.new(key, AES.MODE_CBC)

    # Generate a random IV
    iv = cipher.iv

    # Pad the text to be a multiple of the block size
    padded_text = pad(text.encode(), AES.block_size)

    # Encrypt the padded text
    encrypted_text = cipher.encrypt(padded_text)

    # Return the IV and encrypted text as base64
    return base64.b64encode(iv + encrypted_text).decode()

def decrypt(key, encrypted_data):
    key = key.ljust(32)[:32].encode()  # Pad or truncate key to 32 bytes
    # Decode the base64 encoded data
    encrypted_data = base64.b64decode(encrypted_data)

    # Extract the IV from the beginning
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    padded_text = cipher.decrypt(ciphertext)

    # Unpad the decrypted text
    return unpad(padded_text, AES.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = "my_secret_key"  # Custom key (will be padded/truncated)
    original_message = "Hello, secure world!"

    # Encrypt the message
    encrypted = encrypt(key, original_message)
    print(f"Encrypted: {encrypted}")

    # Decrypt the message
    # decrypted = decrypt(key, encrypted)
    decrypted = decrypt(key, 'X3xU0kkEwGgvMi7CXllZhBoTobTLpy0wLl3YyKTtWbHbOOBmziJDDRIOzvqquizc')
    print(f"Decrypted: {decrypted}")
