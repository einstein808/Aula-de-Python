from Professor import Professor
from Escolaridade import Escolaridade
from Curso import Curso

escolaridade = Escolaridade("Pos-gradução")
professor = Professor("maria")
curso = Curso("computaçao")
professor.setEscolaridade(escolaridade)
curso.setCoordenador(professor)
print(curso.getDescricaoEscolaridadeCoordenador())