import random
import sys

input_user = input("Username: ")
input_account = input("Account for: ")
print("Password length: ")
input_length = input()

password=""

for i in range(int(input_length)):
	asc = random.randint(48, 123)
	password += chr(asc)

filename = "passwords.txt"

pwstring = input_user + "'s " + input_account + " account password: " + password

with open(filename, "a") as f:
	f.write("\n" + pwstring)

print(pwstring)
