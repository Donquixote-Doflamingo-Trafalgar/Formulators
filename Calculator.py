num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (* , + , - or /) = ")
num2 = float(input("Enter the second number: "))
if operator == "/":
    print(f"The result is = {round(num1/num2, 2)}")
elif operator == "*":
    print(f"The result is = {num1*num2}")
elif operator == "+":
    print(f"The result is = {num1+num2}")
elif operator == "-":
    print(f"The result is = {num1-num2}")
else:
    print("The operator is invalid.")