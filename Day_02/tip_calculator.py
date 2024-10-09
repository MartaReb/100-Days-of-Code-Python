print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

bill_per_person = (bill + bill*tip/100)/people
print(f"Each person should pay: $ {bill_per_person:.2f}")