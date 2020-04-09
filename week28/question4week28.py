# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include a simple test function to test the class methods by instantiating an object.
class String():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


testing = String()
testing.getString()
testing.printString()
