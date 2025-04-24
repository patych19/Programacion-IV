def nombre():
    nombre=input("Dime tu nombre: ")
    return nombre
print(nombre())


# ARGUMENTOS POSICIONAL: se asocial al orden por ejemplo nombre apellido y abajo debe cumplirse el mismo orden

def usuario(nombre, edad):
    print("Hola ",nombre, " tienes ",edad)
usuario("Nancy",20)
# ARGUMENTOS NOMINALES:  se puede mandar desordenado 

def usuario(datos):
  nombre = datos["nombre"]
  edad = datos["edad"]
  print("Hola", nombre, "tienes", edad)

usuario({"nombre": "Nancy", "edad": 20})

# ARGUMENTOS POR DEFECTO
# si se anteponen dos ** en el parametro es ---> paso clave falor
def contacto(**info):
   print("Datos del contacto: ")
   for clave, valor in info.items():
    print(clave,":",valor)
contacto

# FUNCIONES RECURSIVAS


