import random
l=[]
list=[random.randint(1,100) for i in range(20)]
print(list)
print(f'average={sum(list)/20}')
mx,mn=max(list),min(list)
print(f'largest number = {mx},smallest number={mn}')
list.remove(mx)
list.remove(mn)
mx,mn=max(list),min(list)
print(f'Largest number={mx},Smallest number={mn}')
for x in list:
    if x%2==0:
        l.append(x)
print(l)        
