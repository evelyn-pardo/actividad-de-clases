#semana28-06-2021

class Ordenar:
    def __init__(self,lista):
        self.lista=lista 
    
    def recorrerElemento(self):   
        for ele in self.lista:
            print(ele)
        
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
   
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])  
            
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele ==  buscado:
                enc=True
                break
        if enc ==True:return pos
        else:return -1
            
       
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)): 
                for sig in range(pos+1,len(self.lista)): 
                    if self.lista[pos] > self.lista[sig]:
                        aux = self.lista[pos]
                        self.lista[pos]=self.lista[sig]
                        self.lista[sig]=aux                   
# ord1.recorrerElemento()
# ord1.recorrerEnumerate()
# ord1.recorrerRange()
# print(ord1.buscar(3))
# buscado=9
# resp = ord1.buscar(buscado)
# if resp !=-1:
#     print("Numero={}se encuentra en la Posicion:({})de la lista:{}".format(buscado,resp, ord1.lista))
# else:
#     print("Numero={} no se encuentra en la lista:{}".format(buscado,ord1.lista))     
    def ordenarDesc(self):
        for pos,ele in enumerate(self.lista):
                for sig in range(pos+1,len(self.lista)): 
                    if ele < self.lista[sig]:
                     aux = self.lista[pos]
                     self.lista[pos]=self.lista[sig]
                     self.lista[sig]=aux
    
    def primer(self):
        return self.lista[0] 
    
    def primerEliminado(self):
        primer = self.lista[0]
        auxilista = []
        for pos in range(1,len(self.lista)):
            auxilista.append(self.lista[pos])
        self.lissta=auxilista
        return primer
    
    def primerEliminado(self):
        primer = self.lista[0]
        self.lissta=self.lista[1:-1]
        return primer
    
    def ultimo(self):
        return self.lista[-1] 
      
    def ultimoEliminado(self):
        ultimo = self.lista[-1]
        self.lissta=self.lista[0:-1]
        return ultimo 
    
    def insertar(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break 
        self.lista=self.lista[0:pos]+auxlista.self.lista[pos:]
    
    def insertar2(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break 
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)   
        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista    
    
    def insertarOrden(self,num):
        self.lista.append(num)
        self.ordenarAsc()
     
    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break 
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        
lista = [2,3,8,10] 
ord1 = Ordenar(lista)
# print(ord1.lista)
# print(ord1.primerEliminado())
if ord1.eliminar(8)==True: print("El numero se elimino de la lista",ord.lista)
else:print("El numero no se encuentra en la lista")

# print("primer",ord1.primer())
# print("segundo",ord1.ultimo())
# print("Normal",ord1.lista)
# ord1.ordenarAsc()
# print("Asc",ord1.lista)
# ord1.ordenarDesc()
# print("Desc",ord1.lista)

