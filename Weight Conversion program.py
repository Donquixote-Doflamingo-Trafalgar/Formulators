Mass = float(input("What's your mass? :   "))
Unit = input("Enter the unit of your weight(Kg or Pounds):")
if Unit == "Kg":
    print(f"Your mass in pounds is {Mass*2.205} ")
elif Unit == "Pounds":
    print(f"Your mass in kilograms is {round(Mass/2.205, 2)} ")
else:
    print("Write only 'Kg'  or  'Pounds' as your Unit input.")