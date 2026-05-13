from cryptography.fernet import Fernet

print("File Encryptor")

# Generate key
key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

choice = input("Enter encrypt or decrypt: ")

file_name = input("Enter file name: ")

try:

    with open(file_name, "rb") as file:
        data = file.read()

    if choice == "encrypt":

        encrypted = fernet.encrypt(data)

        with open(file_name, "wb") as file:
            file.write(encrypted)

        print("File encrypted.")

    elif choice == "decrypt":

        decrypted = fernet.decrypt(data)

        with open(file_name, "wb") as file:
            file.write(decrypted)

        print("File decrypted.")

    else:
        print("Invalid option")

except Exception as e:
    print("Error:", e)