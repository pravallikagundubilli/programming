try:
    a=10
    b=20
    print(a+b+c)
    print(a/0)
except ZeroDivisionError:
    print("cannot divide with zero")
except NameError:
    print('name issue,avoid')
