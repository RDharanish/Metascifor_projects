height = float(input("Enter the height (meter): "))
weight = float(input("Enter the weight (Kilogram): "))
Bmi = weight//(height*height)
print(f"Your BMI is {Bmi}")

with open('bmi.txt','w') as file:
    file.write(f"Your height is {height}m\n")
    file.write(f"your weight is {weight}kg\n")
    file.write(f"your BMI calculator {Bmi}")