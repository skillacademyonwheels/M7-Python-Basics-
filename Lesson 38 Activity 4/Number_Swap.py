# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Swapping the numbers
#num1, num2 = num2, num1
temp = num1
num1 = num2
num2 = temp


# Displaying the swapped numbers
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)