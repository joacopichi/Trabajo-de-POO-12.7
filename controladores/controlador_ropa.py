from dao.dao_ropa import RopaDAO

class ControladorRopa:
    def __init__(self):
        self.ropa_dao = RopaDAO()

    def obtener_toda_ropa(self):
        return self.ropa_dao.obtener_ropa()

    def buscar_ropa_por_nombre(self, nombre):
        return self.ropa_dao.buscar_ropa_por_nombre(nombre)
