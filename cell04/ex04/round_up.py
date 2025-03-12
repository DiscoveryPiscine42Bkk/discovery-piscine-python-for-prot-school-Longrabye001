import math

def round_up(number):

  return math.ceil(number)

number = float(input("Give me a number "))


rounded_number = round_up(number)
print(f"{rounded_number}")
