# menú principal
#flujo del programa
# main.py
# Autor: Nancy Chango


from funciones import registrar_paciente, registrar_consulta, mostrar_paciente, mostrar_todos_pacientes

def main():
    pacientes = {}

    while True:
        print("\n------ Menú Principal ------")
        print("1. Registrar nuevo paciente")
        print("2. Registrar consulta médica")
        print("3. Mostrar datos de un paciente")
        print("4. Mostrar todos los pacientes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente(pacientes)
        elif opcion == "2":
            registrar_consulta(pacientes)
        elif opcion == "3":
            mostrar_paciente(pacientes)
        elif opcion == "4":
            mostrar_todos_pacientes(pacientes)
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
