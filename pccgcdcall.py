def gcd(a,b):
    if b==0:
        return(a)
    else:
        if a>b:
            a,b=b,a
        return(gcd(a,b%a))
a=int(input())
b=int(input())
result=gcd(a,b)
print(result)
