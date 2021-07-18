class Cargo:
   secuencia=0
   def __init__(self,des="Sin Cargo"):
       Cargo.secuencia=Cargo.secuencia+1
       self.codigo=Cargo.secuencia
       self.descripcion=des 
       
cargo1 = Cargo()
print("Ejecutando desde el archivo cargo.py")
print("cargo1",cargo1.codigo,cargo1.descripcion)
cargo2 = Cargo("Docente")
print("cargo2",cargo2.codigo,cargo2.descripcion)
cargo3 = Cargo()
print("cargo3",cargo3.codigo,cargo3.descripcion)
print(Cargo.secuencia)