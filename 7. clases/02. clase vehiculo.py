class Vehiculo:
# Método __init__ para inicializar atributos
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
# Otro método de instancia
    def encender(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} ha encendido")
# Creación de objeto usando __init__
mi_coche = Vehiculo("Toyota", "Corolla", 2022)
# Llamada a un método
mi_coche.encender() # El Toyota Corolla ha encendido