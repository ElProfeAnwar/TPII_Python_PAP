# Definición de la clase
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de ${monto} realizado")
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado")
        else:
            print("Saldo insuficiente")
    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

# Creación de objetos
cuenta1 = CuentaBancaria("Ana García", 1000)
cuenta2 = CuentaBancaria("Carlos López")
# Acceso a atributos
print(f"Titular cuenta 1: {cuenta1.titular}")
print(f"Titular cuenta 2: {cuenta2.titular}")
# Llamada a métodos
cuenta1.mostrar_saldo()
cuenta2.depositar(500)
cuenta2.mostrar_saldo()
cuenta1.retirar(300)
cuenta1.mostrar_saldo()