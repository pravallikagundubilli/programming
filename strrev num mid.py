n=input("Enter the Number")
for i in range(len(n)-1,-1,-1):
    p=n[i]
    print(int(p),end="")
n.reverse()
print(int(n))
