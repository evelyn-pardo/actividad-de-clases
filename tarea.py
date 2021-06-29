
class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        # ciclo repetitivo de incremento o decremento se ejecuta por verdadero 
        nombre = "Daniel"
        datos=["Daniel",50,True]
        numeros=(2,5,6,4,1)
        docente = {'nombre':'daniel','edad': 50,'fac': 'faci'}
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        
        # j=0
        # while j<5:
        #     j=j+1
            
        # for i in range(5): #rango(0,1,2,3,4)
        #     print('for',i,end=" ")
        # print()
        # for i in range(1,5): #rango(1,2,3,4)
        #     print('for',i,end=" ")
        # print()
        # for i in range(2,10,2):#rango(2,4,6,8)
        #     print('for',i,end=" ")
        # print()
        # for i in range(12,3,-3):#rango(12,9,6)
        #     print('for',i,end=" ")
            
             
        # lon = len(nombre)   
        # for pos in range(lon):
        #     if pos%2 == 0 and pos !=0:
        #        print(pos,nombre[pos])
        
        
        # vocal = ('a','e','i','o','u')    
        # for elen in datos:
        #     print(elen,end=" ")
        # for elen in nombre:
        #     print(elen,end=" ")
        
        
        # lon = len(datos)   
        # for pos in range(lon):
        #     print(pos,datos[pos])
            
        # for pos,valor in  enumerate(datos):
        #     print(pos,valor) 
            
        # for clave,valor in docente.items():
        #     print(clave,valor,end=" ")
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     print("for externo", notas)
        #     for nota in notas:
        #         print(nota,end=" ")
        #     print("saliendo del for interno")
            
        # print(listaNotas)
        # for notas in listaNotas:
        #     acum=0
        #     for nota in notas:
        #         acum=acum+nota
        #     print(acum/len(notas),end=" ")
     
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end="  ")
            print()             
bucle = For() 
bucle.usoFor()


