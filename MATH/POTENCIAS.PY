#PROGRAMA QUE CALCULA LA SUMA DE PÓTENCIAS DEL 1 HASTA 1000.

x=1
y=0
suma=0
while x < 1000:
  y= x**x
  x+=1
  suma=suma+y
print(suma)
