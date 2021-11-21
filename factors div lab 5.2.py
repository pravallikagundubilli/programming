import math
n = int(input("enter a number: "))
factors = [1,n]
ci = 1
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        d = n // i
        factors.insert(ci, i)
        if d != i:
            ci += 1
            factors.insert(ci, d)    
print(n)
print(*factors)
