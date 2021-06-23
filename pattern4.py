n=int(input())
for i in range(n,0,-1):
    for j in range(0,n):
        if j<i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
