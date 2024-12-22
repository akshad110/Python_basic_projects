name1 = input("Enter his name: ")
name2 = input("Enter her name: ")

name1.lower()
name2.lower()

name = name1+name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t+r+u+e


l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love = l+o+v+e

love_per = int(str(true)+str(love))
print(f"Your love percentage is: {love_per}")

if love_per <10:
    print("your love is weak.")
elif 10 <= love_per <= 40:
    print("you love is strong.")
elif 50 <= love_per <= 90:
    print("you love is stronger.")
else:
    print("you love is the strongest.")