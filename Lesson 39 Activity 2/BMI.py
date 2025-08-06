print("BMI Calculator")

##inputs
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cms: "))

height = height / 100  # Convert height from cm to meters
bmi = weight / (height ** 2)  # Calculate BMI
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif 30 <= bmi < 34.9:
    print("You have obesity (Class 1).")
elif 35 <= bmi < 39.9:
    print("You have obesity (Class 2).")
elif bmi >= 40:
    print("You have severe obesity (Class 3).")

# End of BMI.py
print("Thank you for using the BMI Calculator!")    
