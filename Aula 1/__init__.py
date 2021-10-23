class Funcionario:
    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

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

funcionario = Funcionario()
funcionario.setNome("marcos")
funcionario.setSalBruto(1200)
funcionario.setTotalDesconto(300)
funcionario.setTotalAcrescimo(400)
print(funcionario.salarioLiquido())

