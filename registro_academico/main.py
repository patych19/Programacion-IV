# main.py
from herramientas import registrar_estudiante, asignar_calificacion, mostrar_estudiante, mostrar_todos_estudiantes

def main():
    while True:
        print("===BIENVENIDOS AL SISTEMA DE EDUCACION=====")
        print("\nMENÚ PRINCIPAL")
        print("1. Registrar estudiante")
        print("2. Asignar calificación")
        print("3. Mostrar información de un estudiante")
        print("4. Mostrar a todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            asignar_calificacion()
        elif opcion == "3":
            mostrar_estudiante()
        elif opcion == "4":
            mostrar_todos_estudiantes()
        elif opcion == "5":
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida. Selecciona del 1 - 5.")

if __name__ == "__main__":
    main()
