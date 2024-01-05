pizza=input("Enter the type of pizza S or M or L - ")

pp = input("Do you want to add Pepperomi? Y or N - ")

chs=input("Do you want to add extra cheese ? Y or N - ")

bill=0

if pizza=='S':
  bill+=15
  if pp=="Y":
    bill+=2
  if chs=="Y":
    bill+=1

if pizza=='M':
  bill+=20
  if pp=="Y":
    bill+=3
  if chs=="Y":
    bill+=1

if pizza=='L':
  bill+=25
  if pp=="Y":
    bill+=3
  if chs=="Y":
    bill+=1

print(f"Your final bill is : {bill}")