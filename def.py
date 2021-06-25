"""funcion sin retorno """

def vocales (frase):
    for car in frase: 
        if car in ('a','e','i','o','u'):
            print (car)
            
"""llamada funcion """
oracion = input('ingrese oracion:')
vocales(oracion.lower())

"""llamada funcion """
def promedio (notas):
    summ=0
    for n in notas: 
        summ += n
    return summ /len (notas)
