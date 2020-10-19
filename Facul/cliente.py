class cliente:
    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._desconto = 0

    def realizar_compra(self):
        pass

    def get_desconto(self):
        return self._desconto
