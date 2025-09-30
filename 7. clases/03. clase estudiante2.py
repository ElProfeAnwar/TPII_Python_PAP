class Estudiante:
# Método __init__ para inicializar atributos
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.asignaturas = []
# Método para inscribir asignatura
    def inscribir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f"{self.nombre} se ha inscrito en {asignatura}")
# Método para mostrar información
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Asignaturas: {','.join(self.asignaturas)}")

# Crear instancia de Estudiante
e1 = Estudiante("Cata Eagle", 18, "Ingeniería civil informática")
e1.inscribir_asignatura("Matemáticas")  
e1.inscribir_asignatura("Programación II")
e1.mostrar_info()
# Crear otra instancia de Estudiante