# clase paciente
# paciente.py
# Autor: Nancy Chango

class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.consultas = []

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta = {}
        consulta["fecha"] = fecha
        consulta["diagnostico"] = diagnostico
        consulta["tratamiento"] = tratamiento

        self.consultas.append(consulta)

    def mostrar_datos(self):
        print("")
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)
        print("Edad:", self.edad)
        print("Tipo de sangre:", self.tipo_sangre)
        print("")

        print("Historial de consultas:")

        if len(self.consultas) == 0:
            print("No hay consultas registradas.")
        else:
            for consulta in self.consultas:
                print("----------------------------")
                print("Fecha:", consulta["fecha"])
                print("Diagnóstico:", consulta["diagnostico"])
                print("Tratamiento:", consulta["tratamiento"])
                print("----------------------------")
