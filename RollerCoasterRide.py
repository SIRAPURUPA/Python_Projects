print("Welcome to roller coaster ride..!")
height = int(input("Enter your height : "))
bill = 0
if height > 120:
  print("Take Ride")
  age = int(input("Enter your age : "))
  
  if age < 12:
    bill = 5
    print("pay $5")
  elif 12 <= age <= 18:
    bill = 7
    print("pay $7")

  elif 45<= age <=55:
    bill=0
    print("Free Ride")
  else:
    bill = 12
    print("pay $12")

  photo = input("Do you want a photo ? yes or no - ")
  if photo == "yes":
    bill += 3
  print(f"Your final bill is {bill}")


else:
  print("Cancel Ride")
