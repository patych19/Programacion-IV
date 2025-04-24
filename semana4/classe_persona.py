class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    

persona1 = Persona("Nancy", 19)
persona2 = Persona("Adrian", 19)

print(persona1.saludar())
print(persona2.saludar())

# implementar la clase hija aqui 
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def datos_completos(self):
        return f"{self.saludar()} Estudio {self.carrera}."
    
est1 = Estudiante("Juan", 20, "Ingeniería")
print(est1.datos_completos())