from hashlib import new
import os, time

#from sqlalchemy import true
#Ejercicio 1
#lista=[]
#n=-15
#while n <= -1:
#    lista.append(n)
#    n = n + 1
#print(lista)

#Ejercicio 2
#n=-15
#par=[]
#while n <= -1:
#    if n % 2 ==0:
#        par.append(n) 
#    n = n + 1
#print(par)

#Ejercicio 3
#mi_list=[]
#[mi_list.append(i) for i in range(-15, -1) if i %2==0 ]
#print(mi_list)

#Ejercicio 4
#print(mi_list)
#marcador = iter(mi_list)
#[print(next(marcador), end=" ") for i in range(0, 3) if i<3]

#Ejercicio 5
#os.system('cls')
#print("Lista Original",sep="\n")
#print(mi_list)
#for i, j in enumerate(mi_list):
#    print()
    #print("{}  {}".format(i, j))

#print("Lista original")
#print(mi_list)
#print()
#[print(i, j) for i, j in enumerate(mi_list) if j]

#Ejercicio 6
#os.system('cls')
#lista=[1,2,3,4,5,6,7,8,10,13,14,15,17,20]
#print(lista)
#for i in range(1, 20):
#    if not i in lista:
#        lista.insert(i-1, i)
#print(lista)
#os.system('cls')#
#lista2=[1,2,3,4,5,6,7,8,10,13,14,15,17,20]
#i = 1
#while i <= 20 :
#    if i not in lista2 :
#        lista2.insert(i-1, i)
#    i+=1    
#print(lista2)      

#Ejercicio 7
#os.system('cls')
#serie=[]
#a=0
#p=1
#s=0
#while s < 999999999999999 :
#    s = a + p
#    a = p
#    p = s
#    serie.append(p)
#    if len(serie)==30:
#        print(f"cantidad de elementos: {len(serie)}")
#        break
#print("Serie Fibonacci")
#print(serie)    
#print()

#Ejercicio 8
#print(sum(serie))

#Ejercicio 9
#os.system('cls')
#i = 0
#cociente=[]
#a=serie[i]
#p=serie[i+1]
#cp = 0
#while  i <= 30:
#    a = serie[i]
#    if i==29:
#        break
#    if i >= 24:
#        p = serie[i+1]##
#        cp = a / p
        #print("{} - {}".format(i, cp))    
#        cociente.append(cp)
#        largo_cociente=len(cociente)    
#    i = i + 1

    #Ejercicio 10
#cadena="Hola Mundo"
#n=[print("posición {} -> {}".format(i, j)) for i, j in enumerate(cadena) if j=='n']

#Ejercicio 11
#dictio={
#         "id":"CX-210",
#         "Nombre":["César","Augusto"],
#         "Residencia":["Argentina", "EE.UU","Japón"]
#}
#for item in dictio.keys():
 #   print("{} ".format(item))

#Ejercicio 12
#lista = list(cadena)
#[print(i, end=" ") for i in lista ]

#Ejercicio 13
#lista1 = [1,-2,3,-4]
#lista2 = ["p", "n", "p", "n"]
#tupla = zip(lista1, lista2)
#print(type(tupla))
#print(list(tupla))

#Ejercicio 14
#lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
#div_siete = []
#[print("{} es divisible por {}".format(i, 7)) for i in lis if i %7 == 0]

#Ejercicio 15
os.system('cls')
print("----------------------------------------------------------------------------------------------------------")
lis = [(2,44,-2),[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
largo=0
acumulador=0
for i in lis:    
    if type(i)==list:
        largo = len(i)    
        acumulador = acumulador + largo
    elif type(i) == tuple:
        largo = len(i)    
        acumulador = acumulador + largo
    elif type(i) == object:
        largo = len(i)    
        acumulador = acumulador + largo
    else:    
        acumulador = acumulador + 1
#print(acumulador)
#print("cantidad de elementos en la lista serie: {}".format(largo_serie))    

#Ejercicio 16
lis = [(2,44,-2),[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i in lis:
    if i != list:
       print(type(list(i)))
       print(i)
    else:
        print("error..")
print()        
#os.system('cls')
[print(type(list(i))) for i in lis if i != list]



    



    




#Iterador, van solo hacia adelante
#nombre = ["Alma", "Mauricio","Nena", "Cesar"]
#marcador = iter(nombre)
#print(next(marcador))
#print(next(marcador))
#print(next(marcador))
#print(next(marcador))
#print(next(marcador))            

#zip
#lista1=[1, 2, 3, 4, 5]
#lista2=["Alma", "Mauricio", "Nena", "Cesar", "Ale"]
#lista3=zip(lista1, lista2)

#print(type(lista3))
#print(lista3)
#print(list(lista3))
#lista="la vida es una moneda, quien la rebusca"
#c = [i for i in lista if i =='a']
#print(c)
#len(c)