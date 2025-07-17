class Huesped:
    def __init__(self, nombre, cedula, email):
        self.nombre = nombre
        self.cedula = cedula
        self.email = email
        self.reservas = []

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Email: {self.email}")
        print("Reservas:")
        for reserva in self.reservas:
            print(f"- {reserva.tipo_habitacion} desde {reserva.fecha_entrada} hasta {reserva.fecha_salida}")
