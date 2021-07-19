##sum of alternate values of a fibonacci series after printing 2
n=int(input("enter a number"))
a=0
b=1
print(2,end=" ")
for i in range(1,n):
    c=a+b
    print(a+c,end=" ")
    a,b=b,c
