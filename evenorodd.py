n=int(input("enter a number"))
if(n%2!=0):
    print("weird")
else:
    if n is range(2,6):
        print("not weird")
    elif n is range(6,21):
        print("weird")
    else:
        print("not weird")
