from Aluno import Aluno
from Escola import Escola
from Estado import Estado


aluno = Aluno("carlos")
escola = Escola("fopddkl")
estado = Estado("jacranda")
escola.setEstadoEscola(estado)
aluno.setEscolaPessoa(escola)
print(aluno.getEstadoEscola())


