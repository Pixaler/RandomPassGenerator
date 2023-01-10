#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("===================================")
print("Welcome to the RandomPassGenerator.")
print("===================================\n")
nr_letters = random.randint(4, 6)
nr_symbols = random.randint(1, 3)
nr_numbers = random.randint(4, 6)

list_password = []
# Fill with letters
for char in range(1, nr_letters + 1):
  list_password += random.choice(letters)

# Fill with numbers
for number in range(1, nr_numbers + 1):
  list_password += random.choice(numbers)

# Fill with symbols
for symbol in range(1, nr_symbols + 1):
  list_password += random.choice(symbols)

# Randomization order
random.shuffle(list_password) # shuffle change order in lists

password = ""
for char in list_password:
  password += char

print(f"Your password is: {password}")