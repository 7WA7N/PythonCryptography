from cryptography.fernet import Fernet
message = 'hello,mynameisali'
key=Fernet.generate_key()
print(key)

fernet_obj=Fernet(key)

encryptedmsg = fernet_obj.encrypt(message.encode())
print(encryptedmsg)

decryptedmsg = fernet_obj.decrypt(encryptedmsg).decode()
print(decryptedmsg)

