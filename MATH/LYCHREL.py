#cantitat de polidromics  per sota de 10000
#teoria de lychrel:

#funció per invertir una cadena
def invertir(variable):
  return variable[::-1]

x=1
y=" "
contador01=0
contador02=0
limit01=1
limit02=1
lychrel=0
while limit01 <= 10000:
  while limit02 < 50: 
    y=x+int(invertir(str(x)))
    if int(y) == int(invertir(str(y))):
      contador01+=1
      limit02=51
    else:
      limit02+=1
      lychrel+=1
      if lychrel==50:
        contador02+=1
  x+=1 
  limit02=0
  lychrel=0
  limit01+=1
  
print("polidromics: ",contador01)
print("lychrel: ",contador02)
if (contador01+contador02) != 10000:
  print("ERROR != 10000: ",contador01+contador02)
else:
  print("Todo salio bien. CODE: ",contador01+contador02)
