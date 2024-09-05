class Estudiante:
    # Método especial __init__ para inicializar los atributos
    def __init__(self, nombre, edad, rut_est):
        self.nombre = nombre
        self.edad = edad
        self.rut_est = rut_est
        self.notas = []  # Lista para almacenar las notas
        self.promedio = 0.0

    # Método para agregar una nota a la lista de notas
    def agregar_nota(self, nota):
        if 1.0 <= nota <= 7.0:
            self.notas.append(nota)
            self.calcular_promedio()
        else:
            print("Nota fuera de rango. Debe estar entre 1.0 y 7.0")

    # Método para calcular el promedio
    def calcular_promedio(self):
        if len(self.notas) > 0:
            self.promedio = sum(self.notas) / len(self.notas)
        else:
            self.promedio = 0.0

    # Método para cambiar el nombre del estudiante
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # Método para cambiar la edad del estudiante
    def cambiar_edad(self, nueva_edad):
        self.edad = nueva_edad

    # Método para mostrar la información del estudiante
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"RUT de Estudiante: {self.rut_est}")
        print(f"Promedio: {self.promedio:.2f}")

# Ejemplo de uso
estudiante1 = Estudiante("Juan Pérez", 16, 12345)
estudiante1.agregar_nota(6.0)
estudiante1.agregar_nota(5.5)
estudiante1.mostrar_info()



"""  Explicación:
Constructor __init__: Inicializa los atributos nombre, edad, numero_estudiante, 
una lista para las notas y el promedio.

Método agregar_nota: Permite añadir una nota válida (de 1.0 a 7.0) y 
llama al método calcular_promedio.

Método calcular_promedio: Calcula el promedio de las notas almacenadas.

Métodos para cambiar el nombre y la edad: Permiten modificar el nombre 
y la edad del estudiante.

Método mostrar_informacion: Imprime toda la información del estudiante.
Este código te permite gestionar la información de un estudiante 
y calcular su promedio de notas 
"""


# Cambiar nombre y edad
estudiante1.cambiar_nombre("Juan P.")
estudiante1.cambiar_edad(17)
estudiante1.mostrar_info()
