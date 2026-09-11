import secrets

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.?/~"

password_length = int(input("How many characters would you like in your password? \n"))

password_list = []

password_list.append(secrets.choice(letters))
password_list.append(secrets.choice(numbers))
password_list.append(secrets.choice(symbols))

all_characters = letters + numbers + symbols

for character in range(password_length - 3):
    password_list.append(secrets.choice(all_characters))

secrets.SystemRandom().shuffle(password_list)

password = ""

for character in password_list:
    password += character

print(f"Your secure password is: {password}")