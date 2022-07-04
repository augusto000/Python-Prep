from veri import Verificaciones
import os, sys 
os.system('cls')

#Ejercicio 1- Ejercicio 2
class Vehiculo():
    def __init__(self, color, tipo, cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada = cilindrada
        self.velocidad=0
        self.direccion=0

    def frenar(self, vel):
        self.velocidad = self.velocidad - vel

    def acelerar(self, vel):
        self.velocidad = self.velocidad + vel

    def doblar(self, grados):
        self.direccion = self.direccion + grados                

    def estado(self):
        print(f"Velocidad : {self.velocidad} - Direccion : {self.direccion}")    

    def detalles(self):
        print(f"Color: {self.color} - tipo: {self.tipo} - cilindrada: {self.cilindrada}")    

#vehiculo = Vehiculo("Marron", "Moto", "1200cm3")
#vehiculo.acelerar(90)
#vehiculo.acelerar(20)
#vehiculo.frenar(40)
#vehiculo.doblar(90)
#vehiculo.estado()
#vehiculo.detalles()

#Ejercicio 5
'''
class Verificaciones():
    def __init__(self, lista, valor, org, dst):
        self.valor = valor
        self.org = org
        self.dst = dst
        self.lista = lista

    def esPrimo(self):
        for j in self.lista:
            c = 0
            if j >= 1:
                for i in range(1, j+1):
                    if (j % i == 0):
                        c = c + 1
                if c == 2:
                    print(f"{j}  es primo:True")
                 
#lista=[3, 4, 11, 7, 5 , 6]    
    def modal(self):
        c = 0
        nro = 0
        n = 0
        for i in self.lista :
            n = self.lista.count(i)        
            if (n > c):
                c = n
                nro = i
        return f"El nro {nro} es el que más se repite {c} veces en la lista"        

    def celsiusAfarenheit(self):
        f = ((self.valor * 9/5) + 32)
        return f"{self.valor}º{self.org} equivale a {round(f,1)} {self.dst}"
    
    def farenAcelsius(self):
        v = (self.valor -32)*5/9
        return f"º{round(self.valor,1)} de {self.org} convertidos a {self.dst} equivale a {round(v, 1)} celsius"    
        
    def celsiusAkelvin(self):
        k = self.valor + 273.15
        return f"º{self.valor}celsius equivale a {round(k, 1)} kelvin"
    
    def kelvinAcelsius(self):
        _kelvinAcelsius=self.valor - 273.15
        return f"{self.valor}º kelvin convertidos a celsius es : {round(_kelvinAcelsius, 1)}"
    
    def kelvinAfaren(self):
            _kelvinAfaren = (self.valor - 273.15) * 9/5 + 32
            return f"{self.valor}º kelvin convertidos a farenheit es : {round(_kelvinAfaren, 1)}"
'''

lista = [3, 4, 11, 7,7,7, 5, 6, 6]        
verificar = Verificaciones(lista, 89, 'C', 'F')
verificar.esPrimo()
print(verificar.modal())
print(verificar.celsiusAfarenheit())
verificar = Verificaciones(lista, 89, 'F', 'C')
print(verificar.farenAcelsius())
verificar = Verificaciones(lista, 89, 'C', 'K')
print(verificar.celsiusAkelvin())
verificar = Verificaciones(lista, 89, 'K', 'C')
print(verificar.kelvinAcelsius())



'''
def main():
    class Animal:
        def __init__(self, especie, edad, color):
            self.especie = especie
            self.edad = edad
            self.color = color

        def hablar(self, texto):
            print(f"....{texto}..")

        def describime(self):
            print("soy de la clase hija", type(self).__name__)        

    class Gato(Animal):
        def __init__(self, especie, edad, color, dueño, raza):
            super().__init__(especie, edad, color)
            self.dueño = dueño
            self.raza = raza
    
    print("---------------------------")
    print(sys.path)
    sys.path.append(r"/mod/modulo")
    print(sys.path)
    print(dir())
    print("---------------------------")
    gato = Gato("Siames ", 4, "Blanco", "Cesar", "Siames Irlandes")
    

if __name__=="__main__":
    main()
'''
'''
def main():

    students = {
            "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
            "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
            "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
            "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
            "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
            "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
        }

    INDEX_NAME=0
    INDEX_SURNAME=1
    INDEX_MAIL=2
    INDEX_CREDITS=3
    total_credit=0

    for key, value in students.items():
        print("------------------------------")
        print(f"given name : {value[INDEX_NAME]}")
        print(f"surname : {value[INDEX_SURNAME]}")
        print(f"credits : {value[INDEX_CREDITS]}")
        total_credit = total_credit + value[INDEX_CREDITS]
    print("------------------------------")    
    print(f"Total credits : {total_credit}")
    
if __name__=="__main__":
    main()
    
'''