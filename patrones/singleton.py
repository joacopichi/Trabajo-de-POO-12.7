class Singleton(type):
    _instancias = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instancias[cls]

class GestorInventario(metaclass=Singleton):
    def __init__(self):
        self.ropa = []

    def agregar_ropa(self, prenda):
        self.ropa.append(prenda)

    def buscar_ropa_por_nombre(self, nombre):
        for prenda in self.ropa:
            if prenda.nombre == nombre:
                return prenda
        return None
