class Tarea:
    def __init__ (self):
        pass
    def CalcularJornada (self):
        ht,he,het= 0,0,0
        ph,phe,pt,ph8= 0,0,0,0
        ht=int(input("Ingrese horas trabajadas:"))
        ph=float(input("Ingrese valor hora:"))
        if ht >40:
            he= ht-40
            if he >8:
                het=he-8
                ph8= 8*ph*2
                phe= het*ph*3
            else:
                phe=0
                ph8=he*ph*2
            pt=40*ph+ph8+phe
        else:
            pt=ht*ph
            print()
        print("sobretiempo<8:{} sobretiempo>8Jornada: {} El pago total de horas es:$ {}".format(ph8,phe,pt))
    
    def factorial(self):
        n = int(input("Ingrese la cantidad de numeros:"))
        for i in range(0):
            numero =int(input("Ingrese numero:"))
            acu=1
            for num in range(numero,1,-1):
                acu= acu*num
            print("numero:{},factorial:{}".format(numero,acu))
tarea = Tarea()
tarea.CalcularJornada()
        