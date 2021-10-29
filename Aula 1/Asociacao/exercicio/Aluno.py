from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)

    def setEscolaAluno(self, escolaAluno):
        self._escolaAluno = escolaAluno

    def getEscolaAluno(self):
        return self._escolaAluno



