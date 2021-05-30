import random
n=int(input("enter the number you want to get"))
r=random.randint(1,100)
print("the number you got is:",r)
if n==r:
    print("u got the number correctly")
else:
    print("sorry,better luck next time")
