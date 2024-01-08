import random

ui=input("What do you choose? Type 0 for rock , 1 for paper or 2 for scissors - ")

cc=random.randint(0,3)

print(f"computer choice : {cc}")

if (ui==0 and cc==0) or (ui==1 and cc==1) or (ui==2 and cc==2):
  print("Both Draw..!")
  
elif (ui==0 and cc==1) or (ui==1 and cc==2) or (ui==2 and cc==0):
  print("You loose..!")

else:
  print("You Win..!")