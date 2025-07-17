from utilidades import registrar_huesped, crear_reserva, mostrar_reservas, mostrar_huespedes
from utilidades import validar_cedula
def main():
    huespedes = []
    reservas = []

    while True:
        print("\n==== BIENVENIDOS AL HOTEL NANCY ====")
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar nuevo huésped")
        print("2. Crear reserva")
        print("3. Mostrar reservas")
        print("4. Mostrar huéspedes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_huesped(huespedes)
        elif opcion == "2":
            crear_reserva(huespedes, reservas)
        elif opcion == "3":
            mostrar_reservas(reservas)
        elif opcion == "4":
            mostrar_huespedes(huespedes)
        elif opcion == "5":
            print("Muchas gracias por su visita. Adiós.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
