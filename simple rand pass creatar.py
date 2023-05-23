import random
password_length = int(input("Enter the desired password length: "))
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+=!@#$&"
password = ''.join(random.sample(characters, password_length))
print(password)
