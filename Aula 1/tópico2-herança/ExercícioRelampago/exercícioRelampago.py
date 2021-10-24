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
    def __init__(self, nome, matricula, titulacao):
        Pessoa.__init__(self, nome,matricula)
        self._titulacao = titulacao

    def getTitulacao(self):
        return self._titulacao

    def setTitulacao(self, titulacao):
        self._titualacao = titulacao



aluno = AlunoEnsinoMedio("carlos","32323322", 60, 80)
professor = Professor("albeto", "333333", "doutor")
print(f"O aluno do ensino médio: {aluno.getNome()}")
print(f"matricula:{aluno.getMatricula()}")
print(f"Cujo professor é: {professor.getTitulacao()} {professor.getNome()}")
print(f"Está = {aluno.setAprovado()}")

print()

aluno2 = AlunoGraducao("vivaldo", "222332", 70, 70)
professor2 = Professor("junior3", "33333", "graduando")

print(f"O aluno da graduação: {aluno2.getNome()}")
print(f"matricula:{aluno2.getMatricula()}")
print(f"Cujo professor é: {professor2.getTitulacao()} {professor2.getNome()}")
print(f"Está = {aluno2.setAprovado()}")