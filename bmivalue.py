height=float(input("Enter your height : "))

weight = int(input("Enter your weight : "))

bmi = weight/(height*height)

if bmi<18.5:
  print(f"Your BMI Value is {bmi}, you are Underweight")
  
elif 18.5<bmi<25:
  print(f"Your BMI Value is {bmi}, you are Normal weight")

elif 25<bmi<30:
  print(f"Your BMI Value is {bmi}, you are Slightly overweight")

elif 30<bmi<35:
  print(f"Your BMI Value is {bmi}, you are Obese")

else:
  print(f"Your BMI Value is {bmi}, you are Clinically Obese")