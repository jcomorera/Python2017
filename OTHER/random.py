#test funció random,shuffle...

import random

def cargar():
  lista=[]
  for x in range(10):
    lista.append(random.randint(0,1000))
  return lista

def imprimir(lista):
	print(lista)

def mezclar(lista):
	random.shuffle(lista)

#main

lista=cargar()
print("lista random")
imprimir(lista)
mezclar(lista)
print("lista shuffle")
imprimir(lista)	  
	
