class Pessoa:
    def __init__(self, nome, email, celular):
        self._nome = nome
        self._email = email
        self._celular = celular
    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome
    def setEmail(self, email):
        self._email = email
    def getEmail(self):
        return self._email
    def setCelular(self, celular):
        self._celular = celular
    def getCelular(self):
        return self._celular


class Funcionario(Pessoa):
    def __init__(self, nome, celular, email, cpf, salario):
        Pessoa.__init__(self, nome, celular, email, )
        self._cpf = cpf
        self._salario = salario

    def setCpf(self, cpf):
        self._cpf = cpf
    def getCpf(self):
        return self._cpf

    def setSalario(self, salario):
        self._salario = salario
    def getSalario(self):
        return self._salario

class Cliente(Pessoa):

    def __init__(self,nome, celular, email, cpf, limiteCredito):
        Pessoa.__init__(self,nome, celular, email,)
        self._cpf = cpf
        self._limiteCredito = limiteCredito

    def setCpf(self, cpf):
            self._cpf = cpf

    def getCpf(self):
            return self._cpf

    def setLimiteCredito(self, limiteCredito):
        self._limiteCredito = limiteCredito
    def getLimiteCredito(self):
        return self._limiteCredito

class Fornecedor(Pessoa):
    def __init__(self,nome, celular, email, cnpj, prazoEntrega):
        Pessoa.__init__(self, nome, celular, email, )
        self._cnpj = cnpj
        self._prazoEntrega = prazoEntrega
    def setCnpj(self,cnpj):
        self._cnpj = cnpj
    def getCnpj(self):
        return self._cnpj

    def getPrazoEntrega(self):
        return self._prazoEntrega
    def setPrazoEntrega(self, prazoEntrega):
        self._prazoEntrega = prazoEntrega

funcionario = Funcionario("carlos", "3299983892", "amodeus@gmail.com", 1234566,1000)
cliente = Cliente("dalila", "3299983892", "amodeus@gmail.com","12455", 2000)
fornecedor = Fornecedor("abc", "3299983892", "amodeus@gmail.com","103983874", 10)
print(f"nome do cliente = {cliente.getNome()}")
print(f"Nome do funcionário é = {funcionario.getNome()}")
print(f"nome da empresa é = {fornecedor.getNome()}")




