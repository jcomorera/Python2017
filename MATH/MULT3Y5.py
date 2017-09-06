#SUMA DE TODOS LOS MULTIPLOS DE 3 Y 5 HASTA 1000.

mult3=3
suma3=0
mult5=5
suma5=0
suma=0
while mult5 < 1000:
  suma5+=mult5
  mult5+=5
while mult3 < 1000:
  suma3+=mult3
  mult3+=3
suma=suma3+suma5
print(suma)
