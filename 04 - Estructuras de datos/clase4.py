import os

from sqlalchemy import values
#Ejercicio 1
ciudades=["Camboya", "Bs As", "Bogotá", "Medellín", "Madrid", "Rio de Janeiro"]
#for item in ciudades:
#    print("{}".format(item))
#print(type(ciudades))   

#Ejercicio 2 
#print(ciudades[1])   

#Ejercicio 3
#
#print(ciudades[1:4])

#Ejercicio 4
#print(type(ciudades))

#Ejercicio 5
#print(ciudades[2:])

#Ejercicio 6
#print(ciudades[:4])

#Ejercicio 7
ciudades.insert(2, "Barcelona")
ciudades.append("Madrid")
#print(ciudades)

#Ejercicio 8
ciudades.insert(3, "San Miguel de Tucumán")
#print(ciudades)

#Ejercicio 9
otra_lista=["Ogden", "Washington"]
ciudades.extend(otra_lista)
print(ciudades)

#Ejercicios 10
_in=0
_in=ciudades.index("Madrid")
#print("indice de ciudad repetida : {}".format(_in))

#Ejercicio 11
_in_=0
#_in_=ciudades.index("jujuy")
#print("indice de ciudad repetida : {}".format(_in_))
#ValueError: 'jujuy' is not in list

#Ejercicio 12
#print(ciudades)
ciudades.remove('Ogden')
#print(ciudades)

#Ejercicio 13
#ciudades.remove('Ogden')
#ValueError: list.remove(x): x not in list

#Ejercicio 14
#ultimo=ciudades.pop()
#print(ultimo)

#Ejercicio 15
os.system('cls')
#print(ciudades * 4)

#Ejercicio 16
#mi_lista=(1, 2, 3, 4, 5, 21, 30, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,31)
#mi_tupla=(mi_lista)
#for n in mi_tupla:
#    print(n)
#print(type(mi_tupla))        

#Ejercicio 17
#for n in mi_tupla:
#    if n >= 10 and n <= 15:
#        print(n)

#Ejercicio 18
#mi_tupla=(mi_lista)
#veinte = 20 in mi_tupla
#treinta = 30 in mi_tupla
#if veinte == True :
#    print("{} ".format(veinte))
#    print("{} si esta en la lista".format("20"))
#else:
#    print("{} ".format(veinte))
#    print("{} no esta en la lista".format("20"))
#if treinta == True:    
#    print("{} ".format(treinta))
#    print("{} si esta en la lista".format("30"))
#else:
#    print("{} ".format(treinta))
#    print("{} no esta en la lista".format("30"))
#Ejercicio 19
#estaParis = "Paris" in ciudades
#if estaParis==True:
#    print("Si se encuentra {}".format("Paris"))
#else:
#    ciudades.append("Paris")
#    print("Se agregó {}".format("Paris"))
#    print(ciudades)    
#    print(estaParis)

#Ejercicio 20
#mi_lista=(1, 2, 3, 4, 5, 21, 30, 8, 9, 31, 31, 3, 13, 14, 15, 16, 17, 18, 19,31)
#mi_tupla=(mi_lista)
#veces_repite_lista = mi_lista.count(3)
#print("en la lista el numero {} se repite {}".format(3, veces_repite_lista))

#veces_repite_tupla = mi_tupla.count(3)
#print("en la tupla el numero {} se repite {}".format(3, veces_repite_tupla))

#Ejercicio 21
mi_lista=(1, 0, 0, 4, 5, 21, 30, 8, 9, 31, 31, 3, 13, 14, 15, 16, 17, 18, 19,31)
mi_tupla=(mi_lista)
#tupla_convertida_a_lista=list(mi_tupla)
#print(type(tupla_convertida_a_lista))

#Ejercicio 22
#elemento1=mi_tupla[0]
#print(elemento1)
#elemento2=mi_tupla[1]
#print(elemento2)
#elemento3=mi_tupla[2]
#print(elemento3)

#Ejercicio 23
os.system('cls')
mi_tupla_=("Ciudad", "Pais", "Continente")
dicc={
    mi_tupla_[0]    :["Camboya", "Bs As", "Bogotá", "Medellín", "Madrid", "Rio de Janeiro"],
    mi_tupla_[1]      :["Vietnan", "Argentina", "Colombia", "Ecuador", "Brasil",   "Espania"],
    mi_tupla_[2]:["Camboya", "Bs As", "Bogotá", "Medellín", "Madrid", "Rio de Janeiro"]
}

#Ejercicio 24
#for item in dicc.keys():
#    clave = item
#    print(clave)

#Ejercicio 25
for key in dicc.keys():
    clave = key
    ciudad = dicc[clave]
    print("{}  : {}".format(clave, ciudad))
    












