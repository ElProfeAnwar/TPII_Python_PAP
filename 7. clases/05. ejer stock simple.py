# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def mostrar_producto(self):
        print(f"Código: {self.codigo}, Nombre: {self.nombre}, Stock: {self.stock}")

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Stock de {self.nombre} aumentado en {cantidad}. Nuevo stock: {self.stock}")

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Stock de {self.nombre} reducido en {cantidad}. Nuevo stock: {self.stock}")
        else:
            print(f"No hay suficiente stock para retirar {cantidad} unidades de {self.nombre}.")


# Clase Categoría
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la categoría {self.nombre}")

    def mostrar_categoria(self):
        print(f"Categoría: {self.nombre}")
        for producto in self.productos:
            producto.mostrar_producto()

# Clase Inventario
class Inventario:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
        print(f"Categoría {categoria.nombre} agregada al inventario")

    def mostrar_inventario(self):
        for categoria in self.categorias:
            categoria.mostrar_categoria()

#_______________Ejemplos de uso_______________________________________________________________________#
# Crear productos
p1 = Producto("001", "Tornillo", 500)
p2 = Producto("002", "Tuerca", 300)

# Crear categoría y agregar productos
cat1 = Categoria("Fijaciones")
cat1.agregar_producto(p1)
cat1.agregar_producto(p2)

# Crear inventario y agregar categorías
inv = Inventario()
inv.agregar_categoria(cat1)



# Mostrar el estado inicial
p1.mostrar_producto()  # Esperado: Código: 001, Nombre: Tornillo, Stock: 10

# Probar aumentar el stock
p1.aumentar_stock(5)  # Esperado: Stock de Tornillo aumentado en 5. Nuevo stock: 15

# Probar reducir el stock con cantidad válida
p1.reducir_stock(8)   # Esperado: Stock de Tornillo reducido en 8. Nuevo stock: 7

# Probar reducir el stock con cantidad mayor al stock disponible
p1.reducir_stock(10)  # Esperado: No hay suficiente stock para retirar 10 unidades de Tornillo.

# Mostrar el estado final
p1.mostrar_producto()  # Esperado: Código: 001, Nombre: Tornillo, Stock: 7

# Mostrar inventario
inv.mostrar_inventario()
