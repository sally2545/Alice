# Calculator program
x = float(input("Enter firstnum"))
z = float(input("Enter secondnum"))
operator = input("Enter operator")
if operator == "+":
    print("The sum is", x + z)
elif operator == "-":
    print("The subtraction is", x - z)
elif operator == "*":
    print("The multiplication is", x * z)
elif operator == "/":
    print("The division is", x / z)
else:
    print("Invalid operator")