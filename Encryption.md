# To incrypt
```
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Get the password from the user
password = input("Enter your password: ")

# Encrypt the password
encrypted_password = fernet.encrypt(password.encode())

# Store the key and encrypted password in a file
with open('passwords.txt', 'w') as f:
    f.write(key.decode() + '\n')
    f.write(encrypted_password.decode())

print("Password encrypted and stored in passwords.txt.")
```

# To decrypt
```
from cryptography.fernet import Fernet

# Read the key and encrypted password from the file
with open('passwords.txt', 'r') as f:
    key = f.readline().strip().encode()
    encrypted_password = f.readline().strip().encode()

# Create a Fernet object with the key
fernet = Fernet(key)

# Decrypt the password
decrypted_password = fernet.decrypt(encrypted_password).decode()

print(f"Decrypted password: {decrypted_password}")
```
