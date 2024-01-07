print("Hey! welcome to the treasure island..")

lr=input("left or right ? - ")
if lr=="right":
  print("Game Over")

else:
  sw=input("swim or wait ? - ")
  if sw=="swim":
    print("Game Over")
  else:
    wd=input("Which Door , Red or Blue or Yellow ? - ")
    if wd =="Red" or wd=="Blue":
      print("Game Over")
    if wd =="Yellow":
      print("YOU WIN!")