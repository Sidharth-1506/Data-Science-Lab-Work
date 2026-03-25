operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        exit()
    result = num1 / num2
else:
    print("Please enter a valid operator")
    exit()

print("Result:", result)