### Planning

The Goal is to create a program that checks if an integer within a range is a prime number.
A prime number is only divisible by itself.

Test all divisors from 2 through n-1
**Version 1**

```.py
def is_prime_v1(n):
 if n == 1:
   return False # 1 is not prime

 for d in range(2, n):
   if n % d == 0:
     return False
 return True
 ```
If function to excludes 1 because it is a unit.
```.py
f n == 1:
   return False # 1 is not prime
```
For loop will check if n is prime by dividing with % operator with numbers in range 2-n. If the answer to the divison is 0, it means the number is divisible by another number that wasnt itself or 0, returning FALSE, if it doesnt occur, TRUE will be returned.

**Version 2**
Test all divisors from 2 through square root of (N)
This version saves time by only dividing and checking numbers 2 until square root of N. When we factor a number as the product of 2 postive integers, arranging it as the first integer as increasing while the second factor is decreasing. It has a perfect factor and every factor that lie after and before this perfect factor are the same. So we just have to test the integers up to the square root of N because afterwards will be redundant.

```.py
import math
import time

def is_prime_v2(n):
if n == 1:
  return False # 1 is not prime

  # Fins the maximum divisor
  max_divisor = math.floor(math.sqrt(n))

  for d in range(2, 1 + max_divisor):
    if n % d ==0:
      return False
    return True

# Test the program
for n in range(1, 21):
  print(n, is_prime_v2(n))
  ```
**Final Version**
Saves time by not checking even divisor so this version only checks odd divisors

```.py
import math 

def is_prime(n): 
# Return 'true' if 'n' is a prime number. False otherwise. 

# If 'n' is 2, it is prime. 
# If 'n' is even and not 2 (ex. 4, 6, 8...), then it is not prime. 
if n == 2: 
  return True
if n > 2 and n % 2 == 0: 
  return False
  
max_divisor = math.floor(math.sqrt(n))
for d in range (3, 1 + max_divisor, 2):
  if n % d == 0:
    return False
  return True 
 ```
This checks if number is even, it checks after the number 2 because number 2 is a prime number
```.py
 # If 'n' is 2, it is prime. 
# If 'n' is even and not 2 (ex. 4, 6, 8...), then it is not prime. 
if n == 2: 
  return True
if n > 2 and n % 2 == 0: 
  return False
```
This gets rid of half of the unnecessary functions by starting at 3; an odd number.
```.py
max_divisor = math.floor(math.sqrt(n))
for d in range (3, 1 + max_divisor, 2):
  if n % d == 0:
    return False
  return True 
```
