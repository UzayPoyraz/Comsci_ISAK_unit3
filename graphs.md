**Graph f(x) = (x+1)^2 - 1, with x from -2, to 2 with 1000 points**

```.py
import matplotlib.pyplot as pyplot
step = 0.04 #nomso explained to me that since it's a 1000 points the difference of 4 from -2 to 2 becomes 0.04
x = []
for i in range(1000):
    x.append(-2 + step*i)
y = [(x+1)**2 - 1 for x in x]

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
```
