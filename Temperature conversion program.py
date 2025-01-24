Degree = float(input("What's the measure of degrees?   "))
Unit = input("What's the unit?   ")
if Unit == "C":
    print(f"The temperature is {(Degree*9/5) + 32} degrees Fahrenheit.")
elif Unit == "F":
    print(f"The temperature is {round((Degree-32)* 5/9, 2)} degrees Celsius")
elif Degree == "" or Unit == "":
    print("The degree or the unit is invalid. Either 'F' or 'C' is accepted.")