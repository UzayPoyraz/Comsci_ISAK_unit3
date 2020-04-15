# Write a Python program that generates random passwords of length 20. The user provides how many passwords should be generated
import random
import string

num = int(input("Enter the number of passwords"))

for i in range(num):
    passwordstring = string.ascii_letters + string.digits + string.punctuation
    passwordlength = 20
    password = "".join([random.choice(passwordstring) for i in range(passwordlength)])
    print(password)

