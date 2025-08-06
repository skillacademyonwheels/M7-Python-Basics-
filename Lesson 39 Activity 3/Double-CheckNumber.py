print("Check a number whether is greayer than 50 or not. If it is, print 'Greater than 50',Check if its Even or Odd otherwise print 'Less than 50'.")

number = int(input("Enter a number: "))

if number > 50:
    print("Greater than 50")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Less than 50")