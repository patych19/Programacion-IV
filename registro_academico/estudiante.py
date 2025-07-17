# sistema que permita registrar estudiantes 
# registro mediante nombre, matricula, carrera
class Estudiante: 
    def __init__(self, nombre, matricula, carrera): 
        self.nombre = nombre 
        self.matricula = matricula 
        self.carrera = carrera
        self.calificaciones = []  # Lista para guardar calificaciones

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_datos_estudiante(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")   
        print(f"Carrera: {self.carrera}")
        print("Calificaciones:")

        for cal in self.calificaciones:
            print(cal)
