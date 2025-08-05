import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password list
password_list = [
    random.choice(letters) for _ in range(nr_letters)
] + [
    random.choice(symbols) for _ in range(nr_symbols)
] + [
    random.choice(numbers) for _ in range(nr_numbers)
]

# Shuffle the password list and join to form the password
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your password is: {password}")
