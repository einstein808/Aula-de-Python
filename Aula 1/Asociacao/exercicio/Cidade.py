class Cidade:
    def __init__(self, nome):
        self._nome = nome
        self.estado = None

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def setEstado(self, estado):
        self._estado = estado

    def getEstado(self):
        return self._estado

    def getNomeEstado(self):
        if self._estado == None:
            return "cidade sem estado"
        else:
            return self._estado.getNome()
