def example():
    global a
    a=12
    print('inside function',a)
a=10
print('before function',a)
example()
print('after function',a)
