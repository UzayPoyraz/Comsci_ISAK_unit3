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
