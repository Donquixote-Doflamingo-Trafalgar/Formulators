P = float(input("What's the money borrowed?:   "))
R = int(input("What's the rate of interest?:   "))
T = float(input("After how many years is it to be returned?:    "))
while P <= 0:
    print("Principal is invalid.")
    P = float(input("What's the money borrowed?:   "))
while R < 0:
    print("Rate of interest cannot be less than 0.")
    R = int(input("What's the rate of interest?:   "))
while T == 0:
    print("Years cannot be 0.")
    T = float(input("After how many years is it to be returned?:    "))
Totalmoneytobereturned = P*pow((1+(R/100)), T)
CI_y = input("Do you want to know the CI seperately? (Y if yes, N if no)   ")
while CI_y == "Y":
    print(f"The amount compounded additionially for {T} year/s is {(Totalmoneytobereturned - P):.2f}.")
    break
    if CI_y == "N":
        print("Okay")
print(f"The money to be returned after {T} year/s is {Totalmoneytobereturned:.2f}.")