import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.?/~"

password_length = int(input("How many characters would you like in your password? \n"))

password_list = []

# Guarantee at least one letter, one number, and one symbol
password_list.append(random.choice(letters))
password_list.append(random.choice(numbers))
password_list.append(random.choice(symbols))

all_characters = letters + numbers + symbols

for character in range(password_length - 3):
    password_list.append(random.choice(all_characters))

random.shuffle(password_list)

password = ""

for character in password_list:
    password += character

print(f"Your password is: {password}")
