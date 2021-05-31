name=input("'enter your name'")
a=len(name)
for i in range(0,a):
    if name[i]=='a':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0 or i==0:
                    print("*",end=" ")
                elif j==2 or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='b':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0 or i==0:
                    print("*",end=" ")
                elif i==2 and j==2:
                    print(" ",end=" ")
                elif j==2 or i==2 or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='c':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if (j==0 or i==0) or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='d':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 and (i==0 or i==4):
                    print(" ",end=" ")
                elif (j==0 or j==2) or (i==4 or i==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='e':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0 or (i==0 or i==2 or i==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='f':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0 or (i==0 or i==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")                
    elif name[i]=='h':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==0 and j==1:
                    print(" ",end=" ")
                elif j==0 or i==0:
                    print("*",end=" ")
                elif j==2 or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='g':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==3 and j==0:
                    print(" ",end=" ")
                elif (j==0 or j==2) or (i==2 or i==4 or i==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='i':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if (i==0 or i==4) or j==1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='j':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==4 and j==2:
                    print(" ",end=" ")
                elif (i==0 or i==4) or j==1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='k':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0:
                    print("*",end=" ")
                elif j==1 and (i==1 or i==3):
                    print("*",end=" ")
                elif j==2 and (i==0 or i==4):
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
    elif name[i]=='l':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==0 or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='m':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 or j==0:
                    print("*",end=" ")
                elif j==1 and (i==1 or i==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='n':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==0 and j==1:
                    print(" ",end=" ")
                elif j==0 or i==0:
                    print("*",end=" ")
                elif j==2 or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='o':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 or j==0 or i==4 or i==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='q':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 or j==0 or i==4 or i==0:
                    print("*",end=" ")
                elif j==1 and i==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")                
    elif name[i]=='p':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 and (i==3 or i==4):
                    print(" ",end=" ")
                elif j==0 or i==0:
                    print("*",end=" ")
                elif j==2 or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='r':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==2 and (i==3 or i==2):
                    print(" ",end=" ")
                elif i==3 and j==1:
                    print("*",end=" ")
                elif j==0 or i==0:
                    print("*",end=" ")
                elif j==2 or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")                
                    
    elif name[i]=='s':
        print("\n")
        for i in range(1,6):
            print("\r")
            for j in range(1,4):
                if(i%2!=0):
                    print("*",end=" ")
                else:
                    if(j==i-1):
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
    elif name[i]=='t':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if j==1 or i==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")                    
    elif name[i]=='u':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if (j==0 or j==2) or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='v':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==4 and (j==0 or j==2):
                    print(" ",end=" ")
                elif (j==0 or j==2) or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='w':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if (j==0 or j==2) or i==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
    elif name[i]=='x':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if (i==0 or i==4) and (j==0 or j==2):
                    print("*",end=" ")
                elif i==2 and j==1:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
    elif name[i]=='y':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==4 and j==2:
                    print(" ",end=" ")
                elif (i==0 or i==4) and (j==0 or j==2):
                    print("*",end=" ")
                elif i==2 and j==1:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")                
    elif name[i]=='z':
        print("\n")
        for i in range(0,5):
            print("\r")
            for j in range(0,3):
                if i==0 or i==4:
                    print("*",end=" ")
                elif i==2 and j==1:
                    print("*",end=" ")    
                else:
                    print(" ",end=" ")
                    
    else:
        print(name)

