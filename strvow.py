
str=input("enter a string")
i=0
c=0
n=len(str)
for i in range(n):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        print("the string contains vowel:",str[i],end="\n")
        c+=1
if c==0:
    print("no vowels in the given string")


            
