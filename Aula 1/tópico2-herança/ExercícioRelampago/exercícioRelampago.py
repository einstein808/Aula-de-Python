class Pessoa:
    def __init__(self, nome, matricula):
     self._nome = nome
     self._matricula = matricula


    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome
    def getMatricula(self):
        return self._matricula
    def setMatricula(self, matricula):
        self._matricula = matricula


class Aluno(Pessoa):
    def __init__(self, nome, matricula, nota1, nota2):
        Pessoa.__init__(self, nome, matricula)

        self._nota1 = nota1
        self._nota2 = nota2

    def getNota1(self):
        return self._nota1
    def setNota1(self, nota1):
        self._nota1 = nota1

    def getNota2(self):
        return self._nota2
    def setNota2(self, nota2):
        self._nota2 = nota2

    def calMediaNotas(self):
        return (self._nota1 + self._nota2)/2

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, matricula, nota1, nota2,):
      Aluno.__init__(self,nome, matricula, nota1, nota2)

    def setAprovado(self):
        if self.calMediaNotas() >= 60:
            return ("Aprovado")
        else:
            return ("Reprovado")
class AlunoGraducao(Aluno):
    def __init__(self, nome, matricula, nota1, nota2):
        Aluno.__init__(self, nome, matricula, nota1,nota2)

    def setAprovado(self):
        if self.calMediaNotas() >= 70:
            return ("aprovado")
        else:
            return ("Reprovado")

class Professor(Pessoa):
    def __init__(self, nome, matricula):
        Pessoa.__init__(self, nome,matricula)

    set


aluno = AlunoEnsinoMedio("carlos","32323322", 60, 80)
print(aluno.setAprovado())