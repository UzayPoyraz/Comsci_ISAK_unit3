# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included). The program should print the dictionary.
x = int(input())
d = dict()
for i in range(1, x + 1):
    d[i] = i * i

print(d)
