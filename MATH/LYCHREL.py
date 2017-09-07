#cantitat de polidromics  per sota de 10000
#teoria de lychrel/algoritmo-196:

def invertir(var):
  return var[::-1]

x=1
y=" "
contador=0
contador01=0
limit=1
limit02=1
lychrel=0
while limit <= 10000:
  while limit02 <= 50: 
    y=x+int(invertir(str(x)))
    if int(y) == int(invertir(str(y))):
      contador+=1
      limit02=51
    else:
      limit02+=1
      lychrel+=1
      if lychrel==50:
        contador01+=1
  x+=1 
  limit02=0
  lychrel=0
  limit+=1
  
print("polidromics: ",contador)
print("lychrel: ",contador01)
if (contador+contador01) != 10000:
  print("ERROR != 10000: ",contador+contador01)
