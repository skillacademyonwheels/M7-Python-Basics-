## Create a Simple Calculator
def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y
def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y    

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# print("Select operation:")
print("Addition Operation: ",add(num1, num2))
print("Subtraction Operation: ",subtract(num1, num2))
print("Multiplication Operation: ",multiply(num1, num2))
print("Division Operation: ",divide(num1, num2))
print("Calculator operations completed successfully.")