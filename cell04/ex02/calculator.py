num1 = input("Give me the first number: ")
num2 = input("Give me the second number: ")


try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 == 0:
    division = 5 
else:
    division = num1 / num2


print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplication}")
