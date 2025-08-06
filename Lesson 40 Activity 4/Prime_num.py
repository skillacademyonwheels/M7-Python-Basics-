print("Find out that the number is prime or not")

input_num = int(input("Enter a number: "))  

for i in range(2, int(input_num**0.5) + 1):
    if input_num % i == 0:
        print(f"{input_num} is not a prime number.")
        break
else:
    print(f"{input_num} is a prime number.")
    