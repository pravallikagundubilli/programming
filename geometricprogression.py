a=int(input("enter the starting value:"))
r=int(input("enter the common ratio:"))
n=int(input("enter the limit of the series"))
print(a,end=" ")
for i in range(1,n):
    m=a*(r**i)
    print(m,end=" ")
            
