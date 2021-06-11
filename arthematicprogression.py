a=int(input("enter the starting value:"))
d=int(input("enter the common difference:"))
n=int(input("enter the range of series"))
print(a,end=" ")
for i in range(1,n):
    s=a+(d*i)
    print(s,end=" ")
