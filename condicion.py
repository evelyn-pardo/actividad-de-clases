class Condicion:

        def _init_(self,num1,num2):
            self.numero1=num1
            self.numero2=num2
            numero = self.numero1+self.numero2
            self.numero3=numero

        def __init__(self,num1,num2):
            self.numero1=num1
            self.numero2=num2
            numero = self.numero1+self.numero2
            self.numero3=numero
            
        def usoif (self):
            if self.numero1==self.numero2:
                 print("numero1:{} y numero2:{} son iguales".format(self.numero1,self.numero2))
            elif self.numero1 < self.numero3:
                 print("numero1:{} es menor numero3:{}".format(self.numero1,self.numero3))
            else:
                 print("no es igual")
            print("fin del metodo")
            
condi1 = Condicion(8,18)
print(condi1.numero3)


class ciclo:

    def _init_(self,numero=10):
        self.numero=numero
        
            
    def usowhile (self):
        print("dentro de clase",self.numero)
        LETRA=""
        while LETRA not in ("a","e","i","o","u"):
            LETRA =input("ingrese una vocal: ").lower()
            #caracter= caracter.lower()

        print("Exelente, es la letra correcta:{} si es vocal".format(LETRA))
ciclo1= ciclo()
print(ciclo1.usowhile())
print("fuera de la clase",ciclo1.numero)
