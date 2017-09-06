#Simple programa que suma los digitos de la seguencia de fibonacci.
#Empezando con 1 y 2 hasta 40000.

x=1
y=2
suma=3
z=0
while z < 40000:
  suma= suma+(y+x)
  if z%2==0:
    x= y+x
  else:
    y=y+x
  z +=1

print(suma)
print("Numero de digitos: ",len(str(suma)))
