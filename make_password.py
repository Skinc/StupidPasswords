import random
import sys

input_user = input("Username: ")
input_account = input("Account for: ")
input_length = input("Password length: ")

password=""

for i in range(int(input_length)):
	asc = random.randint(48, 123)
	password += chr(asc)

filename = "passwords.txt"

with open(filename, "a") as f:
	f.write(input_user + "'s " + input_account + " account password: " + password + "\n")

# print(password)
