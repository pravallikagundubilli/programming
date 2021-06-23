def func(a):
  l=0
  for i in a:
      l+=1
  return(l+func(l-1))
print(func('python'))
