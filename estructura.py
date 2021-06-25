#practica 
numero = 23
apellido = "Pardo"

print(numero,type(numero))
print(apellido,type(apellido))

def mensaje(msg):
    print(msg)

mensaje("Mi primer programa")
mensaje("Mi segundo programa")
 
class Sintaxis:
    intancia =0
    def __init__(self,dato="llamando al constructor1"):
        self.frase=dato
        Sintaxis.intancia = Sintaxis.intancia+1 
print("Sintaxis antes de instancia es:{}".format(Sintaxis.intancia))
ejer1=Sintaxis()
print("Sintaxis de ejer1 es:{}".format(Sintaxis.intancia))
ejer2=Sintaxis("instancia2")
print(ejer1.frase)
print("Sintaxis de ejer2 es : {}".format(Sintaxis.intancia)) 
print("Sintaxis nuevamente de ejer1 es:{}".format(Sintaxis.intancia))
print(ejer2.frase)