class Escola:
    def __init__(self,nome):
        self._nome = nome
        self._diretor = None
    def setDiretor(self, diretor):
        self._diretor = diretor
    def getDiretor(self):
        return self._diretor

    def getEscolaridaDiretor(self):
        if self._diretor == None:
            return "escola sem diretor"
        else:
            return self._diretor.getDescricaoEscolaridade()
