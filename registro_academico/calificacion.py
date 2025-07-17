# asignacion de calificaciones por materia 

class Calificacion:
    
    def __init__(self, materia, nota):
        self.materia = materia  
        self.nota = nota        

    # Función que define cómo se mostrará la calificación si la imprimimos
    def __str__(self):
        texto = f"{self.materia}: {self.nota}"
        return texto
