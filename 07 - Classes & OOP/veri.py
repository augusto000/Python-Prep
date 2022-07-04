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
