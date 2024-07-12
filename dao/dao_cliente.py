class ClienteDAO:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_clientes(self):
        return self.clientes

    def buscar_cliente_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None
