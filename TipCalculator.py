print("Welcome to the tip calculator")
bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, 15 ? "))
people=int(input("How many people to split the bill? "))

bill_wint=tip/100*bill +bill
bill_each=bill_wint/people

print(f"Each person should pay {round(bill_each,2)}")