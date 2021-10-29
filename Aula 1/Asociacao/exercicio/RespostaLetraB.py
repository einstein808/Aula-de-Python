from Professor import Professor
from Escolaridade import Escolaridade
escolaridade = Escolaridade("mestradoss")
professor = Professor("ana")
professor.setEscolaridade(escolaridade)
print(professor.getDescricaoEscolaridade())