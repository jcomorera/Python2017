#calculo del indice de fibonacci que contenga 1000 digitos.

x=1
y=1
z=2
contador=2
contadorx=0
contadory=0

while contadorx <= 1000 or contadory <= 1000:
  contador+=1
  z+=1
  if z%2==0:
    x=y+x
    i=str(x)
    suma=0 
    for e in i:
      contadorx+=1
    if contadorx >= 1000:
      print("resultat:",contador)
    else:
      contadorx=0
  else:
    y=y+x
    i=str(y)
    suma=0 
    for e in i:
      contadory+=1
    if contadory >= 1000:
      print("resultat:",contador)
    else:
      contadory=0
      
