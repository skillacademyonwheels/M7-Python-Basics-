def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number_input = int(input("Enter a non-negative integer: "))

if number_input < 0:
    print("Factorial is not defined for negative numbers.")
elif number_input == 0 or number_input == 1:
    print("Factorial of", number_input, "is 1.")

else:
    result = factorial(number_input)
    print("Factorial of", number_input, "is", result)   