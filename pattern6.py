n=int(input())
k=65
for i in range(0,n):
   for j in range(0,n):
         if  j<i:
            print(chr(k),end=" ")
            k+=1
         elif j==i:
             print(chr(k),end=" ")
             
         else:
            print(" ",end=" ")               
   
   k=k-i
   print()
    
