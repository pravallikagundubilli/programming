n=int(input("enter the value "))
c=0
if n==1:
    print("neither composite nor a prime")
for i in range(2,n):
     if n%i==0:
        c+=1
if c==0:
     print("prime number")
else:
     print("not a prime number")

