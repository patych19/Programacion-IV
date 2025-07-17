# dentro de esta clase se asignan parametros de reverva

class Reserva:
    def __init__(self, huesped, tipo_habitacion, fecha_entrada, fecha_salida):
        self.huesped = huesped
        self.tipo_habitacion = tipo_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def mostrar_datos(self):
        print(f"Huésped: {self.huesped.nombre}")
        print(f"Tipo de habitación: {self.tipo_habitacion}")
        print(f"Fecha de entrada: {self.fecha_entrada}")
        print(f"Fecha de salida: {self.fecha_salida}")
