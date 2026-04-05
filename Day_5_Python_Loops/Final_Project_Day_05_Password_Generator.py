import random
from random import shuffle #--- shuffle in python can only works with lists not strings(unchangeable)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

rand_let = random.choice(letters)
rand_num = random.choice(numbers)
rand_sym = random.choice(symbols)

print("Welcome to the Password Generator")
letters_count = int(input("How many letters you want in the password ? : \n"))
numbers_count = int(input("How many numbers you want in the password ? : \n"))
symbols_count = int(input("How many symbols you want in the password ? : \n"))
password = []

for let in range(0, letters_count) :
    password.append(random.choice(letters))
for num in range(0, numbers_count):
    password.append(random.choice(numbers))
for sym in range(0, symbols_count):
    password.append(random.choice(symbols))
print(password)
# Shuffle
random.shuffle(password)

# sorted
print(sorted(password))
print(password)

pass1 = ""
for i in password :
    pass1 += i
print(pass1)







