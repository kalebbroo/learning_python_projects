# Calculator #

import math


print('''
 _________________________
/  _____________________  \\
| |  _________________  | |
| | |      CALC       | | |
| | |                 | | |
| | |  7  8  9    +   | | |
| | |  4  5  6    -   | | |
| | |  1  2  3    *   | | |
| | |  0  .  =    /   | | |
| | |_________________| | |
| |_____________________| |
|_________________________/
''')
      
print("Welcome to the Cool Calculator!")
print("To use this calculator, please enter the following:")
print("- The first number:")
print("- An operator (+, -, *, /):")
print("- The second number:")
print("")

num1 = float(input("Enter first number:"))
operator = (input("Add the operator:"))
num2 = float(input("Enter second number:"))


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print("Result: ", result)