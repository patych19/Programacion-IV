# registrar pacientes, buscar,agregar,mostrar

# funciones.py
# Autor: Nancy Chango


from paciente import Paciente

def menu_tipo_sangre():
    print("\nSeleccione el tipo de sangre:")
    print("1. O+")
    print("2. O-")
    print("3. A+")
    print("4. A-")
    print("5. B+")
    print("6. B-")
    print("7. AB+")
    print("8. AB-")

    opciones = {
        1: "O+",
        2: "O-",
        3: "A+",
        4: "A-",
        5: "B+",
        6: "B-",
        7: "AB+",
        8: "AB-"
    }

    while True:
        opcion = input("Ingrese una opción: ")

        es_numero = True
        for caracter in opcion:
            if caracter < '0' or caracter > '9':
                es_numero = False

        if es_numero:
            opcion = int(opcion)
            if opcion in opciones:
                return opciones[opcion]
            else:
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Solo números.")

def validar_cedula(cedula, pacientes):
    if len(cedula) != 10:
        print("La cédula debe tener 10 dígitos.")
        return False

    for caracter in cedula:
        if caracter < '0' or caracter > '9':
            print("La cédula solo debe contener números.")
            return False

    if cedula in pacientes:
        print("La cédula ya está registrada.")
        return False

    return True

def validar_nombre(nombre):
    for caracter in nombre:
        if caracter >= '0' and caracter <= '9':
            return False
    return True

def validar_edad(edad):
    es_numero = True
    for caracter in edad:
        if caracter < '0' or caracter > '9':
            es_numero = False

    if es_numero:
        edad = int(edad)
        if edad > 0 and edad <= 100:
            return True
    return False

def validar_fecha(fecha):
    partes = fecha.split("/")

    if len(partes) != 3:
        return False

    dia = partes[0]
    mes = partes[1]
    anio = partes[2]

    # Validar que sean números
    for caracter in dia + mes + anio:
        if caracter < '0' or caracter > '9':
            return False

    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    if dia < 1 or dia > 31:
        return False
    if mes < 1 or mes > 12:
        return False
    if anio < 0 or anio > 2025:
        return False

    return True

def registrar_paciente(pacientes):
    while True:
        nombre = input("Nombre del paciente: ")
        if validar_nombre(nombre):
            break
        else:
            print("Nombre inválido. No debe contener números.")

    while True:
        cedula = input("Cédula: ")
        if validar_cedula(cedula, pacientes):
            break
        else:
            print("Cédula inválida o ya registrada. Intente de nuevo.")

    while True:
        edad = input("Edad: ")
        if validar_edad(edad):
            edad = int(edad)
            break
        else:
            print("Edad inválida. Debe ser un número entre 1 y 100.")

    tipo_sangre = menu_tipo_sangre()

    pacientes[cedula] = Paciente(nombre, cedula, edad, tipo_sangre)
    print("Paciente registrado con éxito.")

def registrar_consulta(pacientes):
    cedula = input("Ingrese la cédula del paciente: ")
    if cedula in pacientes:
        paciente = pacientes[cedula]
        
        while True:
            fecha = input("Fecha de la consulta (dd/mm/aaaa): ")
            if validar_fecha(fecha):
                break
            else:
                print("Fecha inválida. Verifique el día (1-31), mes (1-12) y año (0-2025).")

        diagnostico = input("Diagnóstico: ")
        tratamiento = input("Tratamiento: ")
        paciente.agregar_consulta(fecha, diagnostico, tratamiento)
        print("Consulta registrada.")
    else:
        print("Paciente no encontrado.")

def mostrar_paciente(pacientes):
    cedula = input("Ingrese la cédula del paciente: ")
    if cedula in pacientes:
        paciente = pacientes[cedula]
        paciente.mostrar_datos()
    else:
        print("Paciente no encontrado.")

def mostrar_todos_pacientes(pacientes):
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes.values():
            paciente.mostrar_datos()
