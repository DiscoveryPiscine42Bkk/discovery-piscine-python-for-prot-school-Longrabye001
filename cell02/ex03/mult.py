#!/usr/bin/env python3

# Prompt the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the multiplication result
result = num1 * num2

# Display the multiplication result
print(f"{num1} x {num2} = {result}")

# Determine the sign of the result
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
