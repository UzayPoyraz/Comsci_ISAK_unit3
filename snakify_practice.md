```.py
# This program reads two numbers and prints their sum:
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```
![sum of three](sumofthree.png)

```.py
# Read an integer:
a = int(input())
# Read a float:
b = int(a ** 2)
# Print a value squared:
print(b)
```
![square](square.png)

```.py
# Read the numbers like this:
n = int(input())
k = int(input())
# Print the result with print()
print(k // n)
print(k % n)
```
![applesharing](applesharing.png)

```.py
# Read an integer:
a = int(input())
# Read a float:
b = int(a - 1)
c = int(a + 1)
# Print a value:
print("The next number for the number {} is {}".format(a, c))
print("The previous number for the number {} is {}".format(a, b))
```
![previousandnext](previousandnext.png)

```.py
# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
hour1 = int(input())
minute1 = int(input())
second1 = int(input())
timestamp1 = int((hour1 * 3600) + (minute1 * 60) + second1)
hour2 = int(input())
minute2 = int(input())
second2 = int(input())
timestamp2 = int((hour2 * 3600) + (minute2 * 60) + second2)
moment = int(timestamp2 - timestamp1)
print(moment)
```
![twotimestamps](twotimestamps.png)

```.py
# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
digit = int(a % 10)
print(digit)
```
![lastdigit](lastdigit.png)

```.py
# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(a // 10)
tens = int(b % 10)
print(tens)
```
![tensdigit](tensdigit.png)

```.py
# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
n = int(input())
m = int(input())
days = (m // n)
if ((m % n) == 0):
    print(round(days))
else:
    print(round(days + 1))
``` 
![carroute](carroute.png)

```.py
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)
```
![digitalclock](digitalclock.png)

