n=int(input("enter a number:"))
a=n
s=0
while(n):
    if(n&1==1):
        s+=1
    n=n>>1    
print("the no of 1's in binary representation of",a," is :",s)        
