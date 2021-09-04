s=input()
a=input()
c=a
if a in s:
  b=s.index(a)
  a=a[::-1]
  s=s.replace(c,a)
print(s)
