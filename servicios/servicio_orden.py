from patrones.singleton import GestorInventario

class ServicioOrden:
    def __init__(self):
        self.inventario = GestorInventario()

    def procesar_orden(self, nombre_ropa, cantidad):
        prenda = self.inventario.buscar_ropa_por_nombre(nombre_ropa)
        if prenda and prenda.verificar_disponibilidad(cantidad):
            prenda.actualizar_stock(cantidad)
            return True
        return False
