from Aluno import Aluno
from Cidade import Cidade
from Estado import Estado
estado = Estado("rj")
cidade = Cidade("juiz de fora")
cidade.setEstado(estado)
print(cidade.getNomeEstado())