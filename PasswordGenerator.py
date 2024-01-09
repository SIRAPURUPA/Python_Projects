import random

let = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Welcome to password generator...!")
l = int(input("How many letters would you like ?\n"))
s = int(input("How many symbols would you like ?\n"))
n = int(input("How many numbers would you like ?\n"))

#Easy
# pwd=""

# for i in range(1,l+1):
#   pwd+=random.choice(let)

# for i in range(1,s+1):
#   pwd+=random.choice(sym)

# for i in range(1,n+1):
#   pwd+=str(random.choice(num))

# print(pwd)

# Hard

lis_pwd = []

for i in range(1, l + 1):
  lis_pwd += random.choice(let)

for i in range(1, s + 1):
  lis_pwd += random.choice(sym)

for i in range(1, n + 1):
  lis_pwd += str(random.choice(num))

# print(lis_pwd)
random.shuffle(lis_pwd)
# print(lis_pwd)

final_pwd = ""
for i in lis_pwd:
  final_pwd += i

print(f"Here is your final password {final_pwd}")
