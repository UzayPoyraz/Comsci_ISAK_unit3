# Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
human = int(input("Please input a dog's age in human years: "))

if human < 0:
	print("Incorrect, age must be positive number.")
	exit()
elif human <= 2:
	dog = human * 10.5
else:
	dog = 21 + (human - 2)*4

print("The dog's age in dog's years is", dog)