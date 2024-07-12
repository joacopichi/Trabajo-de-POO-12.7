from dao.dao_cliente import ClienteDAO

class ControladorCliente:
    def __init__(self):
        self.cliente_dao = ClienteDAO()

    def obtener_todos_clientes(self):
        return self.cliente_dao.obtener_clientes()

    def buscar_cliente_por_email(self, email):
        return self.cliente_dao.buscar_cliente_por_email(email)
