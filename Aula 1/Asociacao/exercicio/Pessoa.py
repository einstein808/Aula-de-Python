from Estado import Estado
from Escola import Escola

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._escolaridade = None
        self._naturalidade = None
        self._escolaPessoa = None


    def setEscolaridade(self, escolaridade):
        self._escolaridade = escolaridade
    def getEscolaridade(self):
        return self._escolaridade

    def setNaturalidade(self, naturalidade):
        self._naturalidade = naturalidade
    def getNaturalidade(self):
        return self._naturalidade

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome
    def getDescricaoEscolaridade(self):
        if self._escolaridade == None:
           return "sem escolaridade"
        else:
            return self._escolaridade.getDescricao()

    def getDescricaoNaturalidade(self):
        if self._naturalidade == None:
            return "sem cidade cadastrada"
        else:
            return self._naturalidade.getNome()
    def getEstadoNaturalidade(self):
        return self._naturalidade.getNomeEstado()

    def setEscolaPessoa(self, escolaPessoa):
        self._escolaPessoa = escolaPessoa

    def getEscolaPessoa(self):
        return self._escolaPessoa
    def getEstadoEscola(self):
        return self._escolaPessoa._estadoEscola.getNome()

