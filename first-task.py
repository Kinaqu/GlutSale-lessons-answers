# math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# main_script.py
from math_operations import add, subtract, multiply, divide

num1 = 10
num2 = 5

result_add = add(num1, num2)
result_subtract = subtract(num1, num2)
result_multiply = multiply(num1, num2)
result_divide = divide(num1, num2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
