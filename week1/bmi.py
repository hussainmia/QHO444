name = input("what is your name?")
print(f"hello {name}")

age = int(input("what is your age(years)?"))
print(f"you are {age} years old")

height = float(input("how tall are you in meters?"))
print(f" you are {height} meters tall")

weight = float(input("how much do you weight (in kilograms)?"))
print (f" you weight {weight} kilograms")

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

