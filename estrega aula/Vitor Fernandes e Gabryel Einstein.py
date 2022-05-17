# Questão número 1:
# def soma_vet(vetor):
#     aux = 0
#     tamanho = len(vetor)
#     for x in range(tamanho):
#         aux += vetor[x]
#
#     print(f"A soma de todos os vetores é {aux}")
# soma_vet([1,2,3,4])

# Questão número 2
# def return_carctere(string,numero):
#     tamanho = len(string)
#     if tamanho < numero:
#         print("Invalido")
#     else:
#         aux = ''
#         for x in range(numero + 1):
#             aux += string[x]
#         print(f"O numero escolhido retorna tal parame  : {aux}")
# return_carctere('teste',4)

# Questão número 3
def return_caracteres(string, letra):
    tamanho = len(string)
    aux = ''
    for x in range(tamanho + 1):
        aux += string[x]
        if letra == string[x]:
            final = x
            break

    print(aux)


return_caracteres("teste", "t")
