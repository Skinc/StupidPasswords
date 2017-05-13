import random
import sys

if (len(sys.argv) == 1):
	length = 12
else: 
	length = int(sys.argv[1])

password=""

for i in range(length):
	asc = random.randint(48, 123)
	password += chr(asc)

print(password)
