# Accept two numeric inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Accept the operator input
operation = input("Enter operation (+, -, *, /): ").strip()

# Perform the calculation based on the operation provided
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is undefined."
else:
    result = "Error: Invalid operation."

# Display the output
print(f"Output: {result}")