from Aluno import Aluno
from Escola import Escola
from Estado import Estado
estado = Estado("patinho feio")
aluno = Aluno("vivaldo")
escola = Escola("jose carlos melo")
escola.setEstadoEscola(estado)
aluno.setEscolaAluno(escola)
print(escola.getEstadoEscola())
