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

class Escolaridade:
    def __init__(self, descricao):
        self._descricao = descricao

    def getDescricao(self):
        return self._descricao
    def setDescricao(self, descricao):
        self._descricao = descricao

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._escolaridade = None
        self._naturalidade = None

    def setEscolaridade(self, escolaridade):
        self._escolaridade = escolaridade
    def getEscolaridade(self):
        return self._escolaridade

    def setNaturalidade(self, cidade):
        self._naturalidade = cidade
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

class Professor(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self,nome)

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
    #ndhjdhdhd




#estado = Estado("rj")
# cidade = Cidade("juiz de fora")
# cidade.setEstado(estado)
# print(cidade.getNomeEstado())

# escolaridade = Escolaridade("mestradoss")
# professor = Professor("ana")
# professor.setEscolaridade(escolaridade)
# print(professor.getDescricaoEscolaridade())

escolaridade = Escolaridade("Pos-gradução")
professor = Professor("maria")
curso = Curso("computaçao")
professor.setEscolaridade(escolaridade)
curso.setCoordenador(professor)

print(curso.professor)
