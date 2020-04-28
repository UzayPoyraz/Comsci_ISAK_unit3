| Task Number | Planned Action                                                         | Expected Outcome                                         | Time Estimated | Target Completion                                                                                                                             | Criteria |
|-------------|------------------------------------------------------------------------|----------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 1           | Planning: Meet the client for the first time to understand his needs   | Gain the requirements of the client                      | 20 Minutes     | Clients needs were clear and understood, Will create a Success Criteria and proposed solution to discuss with client in next meeting.         | A        |
| 2           | Planning: Meet with the client to discuss the success criteria         | Gain feedback from client regarding success criteria     | 20 Minutes     | Client was satisfied with the success criteria and nothing is needed to be added. Will create a sketch and design the Application interphase. | A        |
| 3           | Design: Meet with client to discuss the Application interphase created | Gain feedback from client regarding the interphase       | 30 Minutes     | Client was satisfied but needs more artistic design to the app and a registration window to allow him to add other administrators to his app  | B        |
| 4           | Development: Create Window, and adding Functions / Behavior to Buttons | Be able to have a window and buttons working             | 2 Hours        | Window's created and buttons functioning                                                                                                      | C        |
| 5           | Development: Connecting database files                                 | Be able to retrieve data from .csv files                 | 1 Hour         | Data is able to be retrieved                                                                                                                  | C        |
| 6           | Development: Securing the Login                                        | Be able to make login as secure as possible              | 2 Hours        | Passwords are able to be hashed and kept in a .txt file                                                                                       | C        |
| 7           | Development: Edit/Deleting information from Table                      | Be able to change information in Table as client pleases | 2 Hours        | Information in table is able to be altered and saved to be displayed                                                                          | C        |

Record of Tasks
29/1/20
```.py
print("hello world")

#this program checks for an odd even number
# numbers from 1 to 1000

for x in range(1, 1000):
    parity = "odd"
    if x % 2 == 0:
        parity = "even"

    print("{} this number is {}".format(x, parity))

# defining an array or list in phython
# we will calculate the mean, max, and min
val =[34, 4 ,56, 13, 12, 45, 6, 7, 78, 67, 45, 34, 23]
n = len(val)
sum_val = 0
# ind = index
for ind in range(n):
    sum_val += val[ind]
print("the addition is {}".format(sum_val))
sum_val = 0
for ele in val:
    sum_val += ele

print("the addition with second method is", sum_val)

# program that compares 2 numbers and switches place to keep them in order
arr =[3, 39 ,56, 13, 12, 45, 6, 7, 78, 67, 45, 34, 23]

for x in range(n-1):
    ele_left = val[x]
    ele_right = val[x+1]
    print("Current number {}, next number {}".format(ele_left, ele_right))

if ele_left > ele_right:
    print("switch")
```

12/2/20
```.py
import mylib
cities = [(3, 5, 'Paris'), (4, 15, 'Nice'), (8, 6, 'Rome'), (7, 16, 'Budapest')]
d = mylib.distance(cities[0][0], cities[0][1], cities[3][0], cities[3][1])
print("the distance between {} and {} is {}".format(cities[0][2], cities[3][2], d))
```

14/2/20
```.py
# prints extract in upper case
print(extract.upper())

# checks words longer than 5
wordsLong = list(filter(lambda x: len(x) > 5, words))
print(len(wordsLong))
# lambda defines a function

print('#'.join(wordsLong))

for word in words:
    if len(word)>5:
        print('#', word)

total = 0
for letter in extract:
    total += ord(letter)
# The ord() function returns the number representing the unicode code of a specified character

print(total)
```

19/2/20
```.py
customer1 = {'FirstName': 'Filip', 'LastName': 'Keitaro', 'AccNo': '0001', 'Pin': 1119, 'Balance': 5, 'age': 18, 'Contact': 'filip@keitaro.jp'}

def Deposit(CustomerDict, Amount):
    # This functions deposits amount in the customers balance
    CustomerDict['Balance'] += Amount
    print(f'New balance is {CustomerDict["Balance"]}')
```
19/2/20
```.py
import matplotlib.pyplot as pyplot
import math

min = -10
z = []
x = []
y = []
for i in range(2000):
    x.append(min + 0.01*(i + 1))
    y.append(14*math.sin(0.5*x[i]))
    z.append(16*math.cos(0.5*x[i]))

pyplot.plot(z, y)
print(x)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
```
