from huesped import Huesped
from reserva import Reserva



# se verifica que la cedula sea valida es decir
# que tenga 10 digitos contados con el len y verifica que no se repita
def validar_cedula(cedula, huespedes):
    if len(cedula) != 10 : 
        print("La cédula debe tener exactamente 10 dígitos numéricos.")
        return False

    for h in huespedes:
        if h.cedula == cedula:
            print("Esta cédula ya está registrada.")
            return False

    return True
#registrar_huesped(huespedes) permite registrar un nuevo huésped
def registrar_huesped(huespedes):
    nombre = input("Nombre del huésped: ")
    while True:
        cedula = input("Cédula del huésped (10 dígitos): ")
        if validar_cedula(cedula, huespedes):
            break
    email = input("Correo electrónico: ")
    nuevo_huesped = Huesped(nombre, cedula, email)
    huespedes.append(nuevo_huesped)
    print(f"Huésped {nombre} registrado con éxito.")

def crear_reserva(huespedes, reservas):
    print("=== RESERVAS DE HABITACIONES ===")
    if not huespedes:
        print("ERROR! No hay huéspedes registrados.")
        return

    cedula = input("Ingrese la cédula del huésped: ")
    huesped_encontrado = None
    for h in huespedes:
        if h.cedula == cedula:
            huesped_encontrado = h
            break

    if huesped_encontrado is None:
        print("Huésped no encontrado.\n")
        return

    print("\nSeleccione el tipo de habitación:")
    print("1. Normal")
    print("2. Doble")
    print("3. Suite")

    while True:
        opcion = input("Ingrese el número de habitación (1-2-3): ")
        if opcion == "1":
            tipo_habitacion = "Normal"
            break
        elif opcion == "2":
            tipo_habitacion = "Doble"
            break
        elif opcion == "3":
            tipo_habitacion = "Suite"
            break
        else:
            print("Opción inválida. Su opción debe ser del 1 al 3.")

    fecha_entrada = input("Fecha de entrada (dd/mm/aaaa): ")
    fecha_salida = input("Fecha de salida (dd/mm/aaaa): ")

    nueva_reserva = Reserva(huesped_encontrado, tipo_habitacion, fecha_entrada, fecha_salida)
    reservas.append(nueva_reserva)
    huesped_encontrado.reservas.append(nueva_reserva)

    print("\nReserva creada exitosamente para", huesped_encontrado.nombre)
    print("Habitación:", tipo_habitacion)
    print("Entrada:", fecha_entrada, "- Salida:", fecha_salida)
    print()

def mostrar_reservas(reservas):
    if not reservas:
        print("No hay reservas registradas.")
        return

    print("\nReservas registradas:")
    for reserva in reservas:
        print(f"Huésped: {reserva.huesped.nombre}, Entrada: {reserva.fecha_entrada}, Salida: {reserva.fecha_salida}, Tipo de habitación: {reserva.tipo_habitacion}")

def mostrar_huespedes(huespedes):
    if not huespedes:
        print("No hay huéspedes registrados :(")
        return

    print("\nHuéspedes registrados:")
    for h in huespedes:
        print(f"Nombre: {h.nombre}, Cédula: {h.cedula}, Email: {h.email}")
