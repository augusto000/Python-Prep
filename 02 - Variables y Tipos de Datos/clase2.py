import math,os

from regex import P
os.system('cls')

#Ejercicio 1
numZz=float('-32.333')
print(numZz)

#Ejercicio 2
num_f=8.5
print(type(num_f))

#Ejercicio 3
print(type(numZz))
#Ejercicio 4
nombre="augusto"

#Ejercicio 5
num_complejo=2+2j
#Ejercicio 6
print(num_complejo)
#Ejercicio 7
valor_pi=math.pi
print(round(valor_pi,4))

#Ejercicio 8
var1='True'
var2=True
#Ejercicio 9
if var1==var2:
    print(type(var1))
    print(type(var2))
    print("si son lo mismo {} y {}".format(var1,var2))
else:
    print(type(var1))
    print(type(var2))
    print("No son lo mismo distinto tipo {} y {}".format(var1,var2))

#Ejercicio 10
num_entero=-33
numero_decimal=0.33
total= num_entero+numero_decimal
print(total)

#Ejercicio 11
j= 22+3j-2-4j
print(j)

#Ejerciico 12
num_real=0.221
num_complejo=21.5+5j
total=num_real+num_complejo
print(total)

#Ejercicio 13
num1=4
num2=6
r=num1*num2
print(r)

#Ejercicio 14
p=2**8
print(p)

#Ejercicio 15
m=27 / 4
print(m)

 #ejercicio 16
#print(int(m))

#print(round(m,0)," ojo que redondea")

#resto= 27%4
#print(resto)

#ejercicio 18 *obtener 27
#r=(4*int(m))+resto
#print(r)

#Ejercicio 19
#num11=22;num12=0
#resultado=num11+num12
#print(resultado)

print("Ejercicio 20")
value1="2";value2=2

if value1==value2:
   print("son iguales :")
   print(type(value1))
   print(type(value2))
else:    
    print("No son iguales :")
    print(type(value1))
    print(type(value2))

print("Ejercicio 21")
value2 = str(value2)
bandera=False
if value1==value2:
    bandera=True
    print("son iguales {}".format(bandera))
    print(type(value1))
    print(type(value2))
else:
    print("son iguales {}".format(bandera))
    print("No son iguales")    
    print(type(value1))
    print(type(value2))

print("Ejercicio 22")
a = float('3.8')
print("daba error por que habìa una como en vez de un punto")
print(a) 

print("Ejercicio 23")
numero=3
numero-=numero
print(numero)

print("Ejercicio 24")
print("se dezplaza 2 bit a la izquierda y queda 100 en binario, que es la representacion binaria del 4 decimal ")
v = 1 << 2 
print(v)

print("Ejercicio 25")
#se casteo el valor char a int y anduvo
print(2 + int('2'))

print("Ejercicio 26")
numN=99
num_string="1.98"
numZ = float(num_string) - numN
print(numZ)










