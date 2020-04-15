# Write a Python program that asks the user for his first name and last name and a number (1, 100]. The output is a text file with as email addresses for the user:

firstname = input("Enter First Name")
lastname = input("Enter Last Name")
num = int(input("Enter Number between 1 and 100"))
email = open("email.txt", "w")

if 1 < num < 101:
    for i in range(1, num + 1):
        email.write(f"{firstname}.{lastname}{i}@uwcisak.jp\n")

email.close()

