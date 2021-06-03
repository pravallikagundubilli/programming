str1=input("enter string 1")
str2=input("enter string 2 of same length of 1")
a=len(str1);b=len(str2)
if a!=b:
    print("the length of two strings are not same")
else:
    for i in range(a):
        print("{}{}".format(str1[i],str2[i]),end="")

