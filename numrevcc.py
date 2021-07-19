n=int(input("enter a number:"))
res=0
while True:
    r=n%10
    res=res*10+r
    n=n//10
    if n==0:
        break
print("the reverse of the given number is:",res)    
