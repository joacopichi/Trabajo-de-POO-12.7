class Manejador:
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def manejar(self, solicitud):
        if self.sucesor:
            self.sucesor.manejar(solicitud)

class ManejadorStock(Manejador):
    def manejar(self, solicitud):
        if solicitud['cantidad'] > solicitud['ropa'].stock:
            print("Stock no suficiente.")
        else:
            super().manejar(solicitud)

class ManejadorDescuento(Manejador):
    def manejar(self, solicitud):
        solicitud['total'] = solicitud['total'] * 0.9  # 10% de descuento
        super().manejar(solicitud)
