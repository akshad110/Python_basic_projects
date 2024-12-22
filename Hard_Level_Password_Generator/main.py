import random

print("Welcome to password generator.")
l = int(input("How many letters do you want in your passwords: "))
n = int(input("How many numbers do you want in your passwords: "))
s = int(input("How many symbols do you want in your passwords: "))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
          ]
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*','(',')','-','+']
password_list =[]
for i in range(1,l+1):
   char = random.choice(letters)
   password_list += char

for i in range(1,n+1):
   char = random.choice(numbers)
   password_list += char

for i in range(1,s+1):
   char = random.choice(symbols)
   password_list += char
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(password)