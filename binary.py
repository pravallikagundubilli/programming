n=int(input("enter a number:"))

def dectobinary(n):
    b=bin(n)
    l=len(b)
    return(b[l-4])
result=dectobinary(n)
print(result)
