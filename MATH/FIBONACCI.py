#simple sucesión de fibonacci en python.
x=0
print(x)
y=1
print(y)
z=2
while x < 100:
  print(x+y)
  if z%2==0:
    x= y+x
  else:
    y=y+x
  z +=1
