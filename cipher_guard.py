import pyAesCrypt

password = input("Please enter your password to the file: ")

# encrypt
pyAesCrypt.encryptFile("example_text.txt", "example_text.txt.aes", password)

# decrypt
pyAesCrypt.decryptFile("example_text.txt.aes", "example_text_out.txt", password)