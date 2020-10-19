from Facul.cliente import cliente


class clientevip(cliente):
    def __init__(self):
        super().__init__()
        self._desconto = 0.2

    def realizar_compra(self, lista_item):
