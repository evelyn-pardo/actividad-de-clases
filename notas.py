#segunda clase notas 

lista = [4, 6, 8, 8, 11]
prom = (lista)
print('promedio: {} = {}'.format(lista, prom))
x=int(input("Ingrese un numero : "))
if x < 0:
    x= 0
    print("negativo cambiar a cero")
elif x == 0:
    print("cero")
elif x == 1:
    print("uno")
else:
    print("Ninguna opcion")
print("si") if type(x) == int else print("-")