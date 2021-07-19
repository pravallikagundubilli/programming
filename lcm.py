a=int(input("enter a number"))
b=int(input("enter the value of a number"))
i=b
while(i):
    if i%a==0 and i%b==0:
        print("lcm of {},{}={}".format(a,b,i))
        break
    i+=1

