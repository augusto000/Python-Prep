import os
os.system('cls')
#Ejercicio 1
#def esPrimo(n, estado):
#    c = 0
#    if n >= 1:
#        for i in range(1, 101):
#            if (n % i == 0):
#                c = c + 1
#            if c == 2:
#                return n, True         

#c, estado = esPrimo(3,False)    
#print(c, estado)

#Ejercicio 2
#os.system('cls')
#num_generales=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
#num_primos=[]
#def esPrimo(n):
#    c = 0
#    if n >= 1:
#        for i in range(1, 101):
#            if (n % i == 0):
#                c = c + 1                
#        if c == 2:
#            num_primos.append(n)    

#def inputNums():
#    for i in num_generales:
#        esPrimo(i)        
#    print(num_primos)

#inputNums()

#Clase 6 Ejercicio 3 / Ejercicio 4
#Crear una función que al recibir una lista de números,
#devuelva el que más se repite 
# y cuántas veces lo hace.
#  Si hay más de un "más repetido", que devuelva cualquiera
lista_numeros=[1,1,2,2,4,1]
def buscaNumMasRepetidos(lista):
    c=0
    nro=0
    mayor=0
    menor=10
    for i in lista :
        n = lista_numeros.count(i)        
        if (n > c):
            mayor = i
            c = n
            nro = i
        elif (n < c):
            menor = i
    op = int(input("Desea ver el Mayor o el menor de los nros que se repiten 1/2 :"))
    if (op == 1):
        t = f"el mayor o igual de los que se repiten es {mayor}"
        return c, nro, t
    elif (op == 2):
        t = f"el menor que se repite es {menor}"
        return c, nro, t
     
def loadLista():
    os.system('cls')
    x, y, text = buscaNumMasRepetidos(lista_numeros)
#    print("----------------------------------------------------")
#    print("nro {} es el que se repite : {} veces".format(y, x)) 
#    print(f"{text}")
#    print("-----------------------------------------------------")       
loadLista()

#Ejercicio 5
#Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
#Fórmula 1 : (°C × 9/5) + 32 = °F
#Fórmula 2 : °C + 273.15 = °K
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino

def celsiusAfarenheit(valor_grados, text_gr, Faren):
    f = ((valor_grados * 9/5) + 32)
    return f"º{valor_grados} equivale a {round(f,1)} Farenheit"

def farenAcelsius(valor, origen, dst):
    celsius = (valor -32)*5/9
    return f"º{valor} de {origen} convertidos a {dst} equivale a {round(celsius, 1)} celsius"    

def celsiusAkelvin(valor_grados, text_faren, formulaKelvin):
    k = valor_grados + 273.15
    return f"º{valor_grados}celsius equivale a {round(k, 1)} kelvin"

def kelvinAcelsius(valor, origen, dst):
    _kelvinAcelsius=valor-273.15
    print("kelvinAgrados")    
    return f"{valor}º kelvin convertidos a celsius es : {round(_kelvinAcelsius, 1)}"

def kelvinAfaren(valor, origen, dst):
            _kelvinAfaren = (valor - 273.15) * 9/5 + 32
            return f"{valor}º kelvin convertidos a farenheit es : {round(_kelvinAfaren, 1)}"

def ingresar_datos():
    os.system('cls')
    print("Calcular entre celsius a farenheit y kelvin")
    valor = float(input("Ingrese valor : "))
    origen = input("Ingrese medida origen : c / f / k :")
    dst = input("Ingrese medida destino : c / f / k :")
    if origen =='c' and dst=='f':
        celsiusAfaren = celsiusAfarenheit(valor, origen, dst)
#        print("----------------------------------")
#        print(celsiusAfaren)
#        print("----------------------------------")
    elif origen=='f'and dst=='c':
        texto_farenAgrados = farenAcelsius(valor, origen, dst)    
#        print("-----------------------------------")
#        print(texto_farenAgrados)
#        print("-----------------------------------")
    elif origen=='c' and dst=='k':
        celsius_kelvin = celsiusAkelvin(valor, origen, dst)
#        print("-----------------------------------")
#        print(celsius_kelvin)
#        print("-----------------------------------")
    elif origen=='k' and dst == 'c':
        _kelvinAcelsius = kelvinAcelsius(valor, origen, dst)
#        print("-----------------------------------")
#        print(_kelvinAcelsius)    
#        print("-----------------------------------")
    elif origen=='k' and dst == 'f':
        _kelvinAfaren = kelvinAfaren(valor, origen, dst)        
#        print("----------------------------------")
#        print(_kelvinAfaren)    
#        print("----------------------------------")
    else:
        print("Opción inexistente...")    

#ingresar_datos()    

#Ejercicio 6
#Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
def ingresar_datos2():
    temp=[34, 44, 45]
    os.system('cls')
    print("Calcular entre celsius a farenheit y kelvin los valores cargados en la lista")
    for i in temp:
        print(f"el proximo valor es {i}")
        valor = float(i)
        origen = input("Ingrese medida origen : (c / f / k) :")
        dst = input("Ingrese medida destino : f / c / c :")

        if origen =='c' and dst =='f':
                _celsiusAfaren = celsiusAfarenheit(valor, origen, dst)
                print("----------------------------------")
                print(_celsiusAfaren)
                print("----------------------------------")    
        elif origen=='f' and dst =='c':
                texto_farenAgrados = farenAcelsius(valor, origen, dst)    
                print("-----------------------------------")
                print(texto_farenAgrados)
                print("-----------------------------------")
        elif origen=='k' and dst == 'c':
                _kelvinAcelsius = kelvinAcelsius(valor, origen, dst)
                print("-----------------------------------")
                print(_kelvinAcelsius)    
                print("-----------------------------------")        
        else:
            print("---------------------------------------")
            print("Opción inexistente..")
            print("---------------------------------------")
#ingresar_datos2()

#Ejercicio 7
#Armar una función que devuelva el factorial de un número. 
#Tener en cuenta que el usuario puede equivocarse 
#y enviar de parámetro un número no entero o negativo

print("Factorial de un número")

def calcularFactorial(n):
    r=1
    while n > 0:
        print(f"{r} * {n}")
        r = r * n        
        n = n - 1  
    return r  

def ingresar_datos3():
    op=True
    while op:
        n = int(input("Ingresar un numero :"))
        if (n > 0 ):
            r = calcularFactorial(n)
            print("------------------------------------")
            print(f"El factorial de {n} es {r}")
            print("------------------------------------")
        else:
            print("----------------------------------------------")
            print("Debe ingresar valores mayores que cero")    
            print("----------------------------------------------")
        
        resp=input("Desea ingresar otro nro ? : s / n :")
        if resp.lower()!='s':
            print("Muchas Gracias!!")
            op=False
        
ingresar_datos3()







