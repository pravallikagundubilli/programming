n=int(input("enter the number:"))
p=int(input("enter the position of 1"))
n=n>>(p-1)
if(n&1==1):
    print("Yes")
else:
    print("No")
