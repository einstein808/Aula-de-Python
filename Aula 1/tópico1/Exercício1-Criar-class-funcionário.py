class Funcionario:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome
        self._salarioBruto = salarioBruto
        self._totalAcrescimo = totalAcrescimo
        self._totalDesconto = totalDesconto

    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome
    def setSobrenome(self, sobrenome):
        self._sobrenome = sobrenome
    def getSobrenome(self):
        return self._sobrenome

    def setSalBruto(self, salarioBruto):
        self._salarioBruto = salarioBruto

    def getSalBruto(self):
        return self._salarioBruto

    def setTotalAcrescimo(self, totalAcrescimo):
        self._totalAcrescimo = totalAcrescimo

    def getTotalAcrescimo(self):
        return self._totalAcrescimo

    def setTotalDesconto(self, totalDesconto):
        self._totalDesconto = totalDesconto

    def getTotalDesconto(self):
        return self._totalDesconto

    def salarioLiquido(self):
      return self._salarioBruto + self._totalAcrescimo - self._totalDesconto

nome = input("Digite seu sobrenome")
sobrenome = input("Digite seu sobrenome")
salarioBruto = int(input("Digite seu salário Bruto"))
totalAcrescimo = int(input("Digite total de acréscimos"))
totalDesconto = int(input("Digite total de descontos"))

funcionario = Funcionario(nome, sobrenome)
funcionario.setTotalDesconto(totalDesconto)
funcionario.setTotalAcrescimo(totalAcrescimo)
funcionario.setSalBruto(salarioBruto)
print()
print(f"O salário Liquido de {funcionario.getNome()} {funcionario.getSobrenome()} é = R${funcionario.salarioLiquido()}.")


