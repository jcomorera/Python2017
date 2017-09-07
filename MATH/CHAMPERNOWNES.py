#fracción irracional, concatenacio de nombres enters.
#exemple: 0,123456789010(1)121314  -->  d12=1

#calcul de la seguent operació: d1*d10*d100*d1000*d10000*d100000*d1000000

x=1
cadena=" "
while x < 1000000:
  cadena+= str(x)
  x+=1

i1=int(cadena[1:2])             #d1
i2=int(cadena[10:11])           #d10 
i3=int(cadena[100:101])         #d100
i4=int(cadena[1000:1001])       #d1000
i5=int(cadena[10000:10001])     #d10000
i6=int(cadena[100000:100001])   #d100000
i7=int(cadena[1000000:1000001]) #d1000000

print(i1*i2*i3*i4*i5*i6*i7)


