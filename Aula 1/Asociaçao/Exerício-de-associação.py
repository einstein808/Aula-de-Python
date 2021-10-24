class Estado:
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return  self._nome

    def seNome(self, nome):
        self._nome = nome

class Cidade:
    def __init__(self, nome):
        self._nome = nome
        self.estado = None

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def getNomeEstado(self):
        if self.estado == None:
            return "cidade sem estado"
        else:
            return self.estado.getNome()


estado = Estado("rj")
cidade = Cidade("juiz de fora")
cidade.setEstado(estado)
print(cidade.getNomeEstado())