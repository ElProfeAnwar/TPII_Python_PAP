class Estudiante:
    # Atributo de clase
    universidad = "San Sebastián"
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
# Creación de objetos
e1 = Estudiante("Ana", 20)
e2 = Estudiante("Carlos", 22)

# Acceso a atributos
print(e1.nombre) # Ana
print(e2.nombre) # Carlos
print(e1.universidad) # San Sebastián
print(e2.universidad) # San Sebastián