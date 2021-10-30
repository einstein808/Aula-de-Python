




from Aluno import Aluno
from Cidade import Cidade
from Estado import Estado









estado = Estado("calos nddobrega")
aluno = Aluno("carlos")
naturalidade = Cidade("carmos de minas")
naturalidade.setEstado(estado)
aluno.setNaturalidade(naturalidade)
print(aluno.getEstadoNaturalidade())