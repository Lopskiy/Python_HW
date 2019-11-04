class MyError(Exception):
    def __init__(self, text):
        self.txt = text


a = input("Input first number: ")
b = input("Input second number: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError("Division by Zero")
except ValueError:
    print("Error type of value!")
except MyError as mr:
    print(mr)
else:
    print(a / b)
