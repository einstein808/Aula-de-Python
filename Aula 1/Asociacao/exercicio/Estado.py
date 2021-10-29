class Estado:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return  self._nome

    def seNome(self, nome):
        self._nome = nome