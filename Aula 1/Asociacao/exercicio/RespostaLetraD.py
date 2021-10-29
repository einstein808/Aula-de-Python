from Professor import Professor
from Escolaridade import Escolaridade
from Escola import Escola

escolaridade = Escolaridade("doutorado")
professor = Professor("adalberto")
escola = Escola("machado")
professor.setEscolaridade(escolaridade)
escola.setDiretor(professor)
print(escola.getEscolaridaDiretor())