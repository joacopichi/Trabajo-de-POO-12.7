class Ropa:
    def __init__(self, nombre, precio, talla, stock):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad

    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad
