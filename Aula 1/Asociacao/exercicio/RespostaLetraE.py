from Cidade import Cidade
from Estado import Estado
from Professor import Professor
professor = Professor("adalberto")
naturalidade = Cidade("juiz de fora")
professor.setNaturalidade(naturalidade)
print(professor.getDescricaoNaturalidade())


