age = int(input("Enter your age: "))
member = input("Are you a member? Type Yes or No: ").strip().lower()

if age < 18:
    if member == "yes":
        print("The fee is 450.00 pesos")
    else:
        print ("The fee is 650.00 pesos")
elif age >= 18 and age <= 65:
    if member == "yes":
        print ("The fee is 550.00 pesos")
    else:
        print("The fee is 750.00 pesos")
elif age >= 65 and age <= 100:
    if member == "yes":
        print ("The fee is 400.00 pesos")
    else:
        print("The fee is 600.00 pesos")
else:
    print("invalid")    