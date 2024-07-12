class RopaDAO:
    def __init__(self):
        self.ropa = []

    def agregar_ropa(self, prenda):
        self.ropa.append(prenda)

    def obtener_ropa(self):
        return self.ropa

    def buscar_ropa_por_nombre(self, nombre):
        for prenda in self.ropa:
            if prenda.nombre == nombre:
                return prenda
        return None
