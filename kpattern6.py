n=int(input('enter'))
k=97
for i in range(n,0,-1):
     for j in range(1,i+1):
          print(chr(k),end=' ')
          k+=1
     print('\n')
