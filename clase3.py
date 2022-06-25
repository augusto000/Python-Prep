import os
os.system('cls')

#Ejercicio -3
#palabra="Python"
#for letra in palabra:
#    if letra =="o":
#        print()
#        continue
#        print(letra)
#    else:
#        print(letra)    


#Ejercicio -2
#x=5
#while True:
#    print(x)
#    x-=1
#    if x==0:
#        print(x)
#        break

#Ejercicio -1

#cadena="Python"
#for letra in cadena:
#    if letra =='h':
#        print("se encontro la letra")
#        print(letra)    
#        break

 #Ejercicio 0 
 #encontrar si es primo el nro
#value=int(input("Ingrese valor :"))
#c=0
#for n in range(1, value+1):
#    if value % n==0:
#        c+=1
#if c==2:
 #   print("{} es primo".format(value))
#else:
 #   print("{} No es primo".format(value))
 #   print(c)

#Ejercicio 1
#value =-3
#if value > 0:
#    print("{} es mayour que 0".format(value))
#elif value < 0:
#    print("{} es menor que 0".format(value))
#else:
#    print("es cero (0)")    

#Ejercicio 2
#num1=4+2j
#num2=6
#num1=type(num1)
#num2=type(num2)

#if num1 == num2:
#    print("Son iguales")
#    print("tipo de num1 {}".format(num1))
#    print("tipo de num2 {}".format(num2))
#else:
#    print("No son iguales")
#    print("tipo de num1 {}".format(num1))
#    print("tipo de num2 {}".format(num2))

#Ejercicio 3
#for n in range(1, 21):
#    if n % 2 == 0:
#        print("{} es par".format(n))
#    else:
#        print("{} es impar".format(n))

#Ejercicio 4
#for n in range(1, 10):
#    if n <= 5:
#        cubo = (n * n * n)
#        print("{} elevado a {} es {}".format(n, 3, cubo))
#    else:
#        print("{} ".format(n))    

#Ejercicio 5
#numZ=-6
#for n in range(numZ, 1):
#    print("Ciclo {}".format(n))

#Ejercicio 6
#f=int(input("Ingrese un numero para calcular su factorial  :"))
#fact=1
#while f > 0:
#    fact = fact * f
#    f -= 1
#print("{} ".format(fact))    

#Ejercicio 7
#subtotal=0
#op=True
#while op:
#    for n in range(1, 5):
#        subtotal= subtotal + n
#        if n==4:
#            print("subtotal {}".format(subtotal))
#            print("valor de n -> {}".format(n))
#            print("fin")
#            op = False
            
#Ejercicio 8
#palabra = "Python"
#for n in palabra:
#    while n != 't':
#        break
#    else:
#        print(n.upper())
#        break

#Ejercicio 9
#def esPrimo(lprimos):
#   j=1
#    c=0
#    for n in lprimos:
#        while j <= 30:
#           if n % j==0:
#                c = c+1
#            j = j + 1    
#        if c == 2:
#            print("{}  es primo".format(n))    
#        else:
#            print("{} No es primo".format(n))    
#        #vuelvo variables a su valor original
#        j=1
#        c=0
#lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#lPrimos=lista
#llamo a función para averiguar si el nro de la lista es primo
#esPrimo(lPrimos)

#Ejercicio 10 - Clase 3
#¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó
#continue para tal fin
#def esPrimo(lnros, arrPrimos):
#    j=1
#    c=0
#    for n in lnros:
#        while j <= 30:
#            if n ==0 or n==1 or n==6 or n==8 or n==9 or n==10 or n==12 or n==14 or n==15 or n==16\
#                or n==18 or n==20 or n==21 or n==22 or n==24 or n==25 or n==26 or n==27 or n==28 or \
#                    n==30:
#                break
#            else:      
#                if n % j==0:
#                    c = c+1
#            j = j + 1    
#        if c == 2:
#            arrPrimos.append(n)           
#        else:
#            print("{} no es primo".format(n))           
        #vuelvo variables a su valor original
#        j=1
#        c=0
#    return arrPrimos
#lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#cargar en variable lnros la lista de todos los nros
#lnros=lista
#pri se encarga de guardar los nro primos y se lo pasa como augumento de esPrimo
#pri=pri=[]
#llamo a función para averiguar si el nro de la lista es primo
#arrPri=esPrimo(lnros, pri)
#print()
#print("Numeros primos :")
#for n in arrPri:
#    print(n)

#Ejercicio 11
#Los numeros que no son primos la sentencia if los evalua para hacerles break, se rompe el bucle y se sigue con el 
#siguiente nro de la lista donde estan todos los nros, tanto los primos como los que no son.
######################################################################################################################
#### Saltea los que no son primos ####################################################################################
#if n ==0 or n==1 or n==6 or n==8 or n==9 or n==10 or n==12 or n==14 or n==15 or n==16\
#                or n==18 or n==20 or n==21 or n==22 or n==24 or n==25 or n==26 or n==27 or n==28 or \
#                    n==30:
#                break
#            else:      
#                if n % j==0:
#                    c = c+1
#            j = j + 1    
#        if c == 2:
#            arrPrimos.append(n)           
#        else:
#            print("{} no es primo".format(n))           

#Ejerciio 12
#def esPrimo(lnros, arrPrimos):
#    j=1
#    c=0
#    for n in lnros:
#        while j <= 40:
#            if n ==0 or n==1 or n==6 or n==8 or n==9 or n==10 or n==12 or n==14 or n==15 or n==16\
#                or n==18 or n==20 or n==21 or n==22 or n==24 or n==25 or n==26 or n==27 or n==28 or \
#                    n==30 or n==32 or n==33 or n==34 or n==35 or n==36 or n==38 or n==39 or n==40:
#                break
#            else:      
#                if n % j==0:
#                    c = c+1
#            j = j + 1    
#        if c == 2:
#            arrPrimos.append(n)           
#        else:
#            print("{} no es primo".format(n))           
        #vuelvo variables a su valor original
#        j=1
#        c=0
#    return arrPrimos
#lista general de todos los numeros
#lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

#cargar en variable lnros la lista de todos los nros
#lnros=lista

#pri se encarga de guardar los nro primos y se lo pasa como augumento de esPrimo
#pri=pri=[]

#llamo a función para averiguar si el nro de la lista es primo
#arrPri=esPrimo(lnros, pri)

#print()
#print("Numeros primos :")
#for n in arrPri:
#    print(n)      

#Ejercicio 13
#n=100
#divi_doce=[]
#rango
#while n >= 100 and n <= 300:
#    if n % 12 == 0:
#        divi_doce.append(n)
#        n = n + 1
#    else:
#        n = n + 1
#        continue 
#        print("{} No es divisible".format(n))   
#Imprime nros divisibles por 12
#for i in divi_doce :
#    print("{} es divisible por 12 ".format(i))    

#Ejercicio 14
#c=0
#prim=[]
#op=True
#while op:
#    num = int(input("Ingrese numero para saber si es primo : "))
#    for i in range(1, 30):
#        if num % i == 0:
#            c = c + 1
#    if c == 2:
#        prim.append(num)
#        print("{} es primo".format(num))
#    else:
#        print("{} No es primo".format(num))    
#    c=0       
#    r = input("Desea ingresar otro numero ? s/n: ")
#    if r.lower()=='s':
#        op=True
#    else:
#        op=False
#        print(prim)  
#Ejercicio 15
#num=100
#div_tres=[]
#c=0
#while num >=100 and num <=300:
#    if num %3 == 0 and num %6== 0 :#divisible por 3
#         mul6= num * 6 #multiple de 6
#         div_tres.append(num)
#         break        

#    num = num + 1
#print("{} es divisible por 3".format(div_tres))
#print("{} es multiplo de {}".format(mul6, 6))




    
    
    

    
    
