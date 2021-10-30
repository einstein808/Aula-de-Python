class Curso:
    def __init__(self,nome):
        self._nome = nome
        self._coordenador = None

    def getNome(self):
            return self._nome

    def seNome(self, nome):
            self._nome = nome

    def getCoordenador(self):
        return self._coordenador
    def setCoordenador(self, coordenador):
        self._coordenador = coordenador


    def getDescricaoEscolaridadeCoordenador(self):
        if self._coordenador == None:
            return "Coordenador sem escolaridade"
        else:
            return self._coordenador.getDescricaoEscolaridade()



