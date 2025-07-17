# herramientas.py
from estudiante import Estudiante
from calificacion import Calificacion

estudiantes = []

def validar_matricula(matricula, estudiantes):
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            print("La matrícula ya está registrada")
            return False
    return True

def registrar_estudiante():
    nombre = input("Ingrese el nombre y apellido: ")
    while True:
        matricula = input("Ingrese la matrícula: ")
        if validar_matricula(matricula, estudiantes):  
            break
    carrera = input("Ingrese la carrera: ")
    estudiante = Estudiante(nombre, matricula, carrera)
    estudiantes.append(estudiante)
    print("Estudiante registrado. ¡BIENVENIDO!")

def buscar_estudiante(matricula):
    for estudiante in estudiantes:
        if estudiante.matricula == matricula:
            return estudiante
    return None

def asignar_calificacion():
    matricula = input("Ingrese la matrícula: ")
    estudiante = buscar_estudiante(matricula)
    if estudiante:
        print("\nSeleccione la materia:")
        print("1. Redes")
        print("2. Programación")
        print("3. Sistemas")
        print("4. Infraestructura")
        print("5. Física")
        
        materias = {
            "1": "Redes",
            "2": "Programación",
            "3": "Sistemas",
            "4": "Infraestructura",
            "5": "Física"
        }

        while True:
            opcion = input("Seleccione del 1 - 5: ")
            if opcion in materias:
                materia = materias[opcion]
                break
            else:
                print("Opción inválida. Intente de nuevo.")

        while True:
            try:
                nota = float(input("Ingrese la nota : "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Ingrese un número válido.")

        calificacion = Calificacion(materia, nota)
        estudiante.agregar_calificacion(calificacion)
        print("Calificación registrada.")
    else:
        print("Estudiante no encontrado.")

def mostrar_estudiante():
    matricula = input("Ingrese la matrícula: ")
    estudiante = buscar_estudiante(matricula)
    if estudiante:
        estudiante.mostrar_datos_estudiante()
    else:
        print("Estudiante no encontrado.")  

def mostrar_todos_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    for estudiante in estudiantes:
        estudiante.mostrar_datos_estudiante()
