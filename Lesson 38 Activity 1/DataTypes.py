name = "Penguin"
age = 5
is_True = True
weight = 30.5

print("Name:", name)
print("Age:", age)  
print("Is True:", is_True)
print("Weight:", weight)

print("====== Type checks ======")
print("Type of name:", type(name))
print("Type of age:", type(age))    
print("Type of is_True:", type(is_True))
print("Type of weight:", type(weight))
print("====== Type conversions ======")
print("Converted age to string:", str(age))
print("Converted weight to integer:", int(weight))
print("Converted is_True to integer:", int(is_True))    
print("Converted name to boolean:", bool(name))  # Non-empty string is True