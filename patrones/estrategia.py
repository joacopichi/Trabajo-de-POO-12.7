class EstrategiaDescuento:
    def aplicar_descuento(self, total):
        raise NotImplementedError("Este método debe ser sobrescrito.")

class SinDescuento(EstrategiaDescuento):
    def aplicar_descuento(self, total):
        return total

class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar_descuento(self, total):
        return total * (1 - self.porcentaje / 100)
