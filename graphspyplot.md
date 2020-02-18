**graphspyplot.py**

```.py
import matplotlib.pyplot as pyplot
import random

x = [i for i in range(1, 1000)]
y = list()
for i in x:
    y.append(random.randint(1, 100))

pyplot.plot(x, y)

pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
```

**randaverage**

```.py
import random
x = []
total = 0
for i in range (0, 1000):
    x.append(random.randint(1, 100))
    total += x[i]
average = (total/1000)
print(average)
```

**wavegraph**

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

pyplot.plot(x, y,)
print(x)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
```

**circlegraph(?)**

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
