class Ciclo:
    def __init__(self,numero=5):
        self.numero*numero
        self.numero2=0 
    
    def usowhile(self):
        # ciclo repetitivo que se ejecuta la condicion se cumple(verdaddero),
        # es decir sale por falso 
        car = input("ingrese vocal")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car1 = input("ingrese vocal").lower()
            
        for car in('a','e','i','o','u'):
            print(car)   
        print("Felicitaciones su vocal es:{}'.format(car)")
        
        
        
ciclo1= Ciclo()
ciclo1.usowhile()
print("fin de uso ciclo")