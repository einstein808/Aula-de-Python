# def CadastrarUsuario():
#     nome = input("digite seu nome")
#     peso = float(input("digite o seu peso em kilos"))
#     altura = float(input("digite sua altura em metros"))
#     cpf = float(input("digite o seu cpf"))
#     resultadp = peso / altura**2
#     return f"olá {nome}, cujo cpf é: {cpf}. Seu imc é {resultadp:.2f}"


# print(CadastrarUsuario())

# def VerPolidromo():
#     string = input("digite a palavra")
#     tamanho = len(string)
#     esquerda = list(reversed(string))
#     cont = 0
#     for x in range(tamanho):
#         if esquerda[x] == string[x]:
#             cont += 1
#         else:
#             break

#     if cont == tamanho:
#         return "é Polidromo"
#     else:
#         return "nao é polidromo"


# print(VerPolidromo())

def SepararNumeros():
    contq = int(input("digite qual tamanho do vetor"))
    valor = input(f"digite o numero com {contq} de tamanho")
    final = []
    while len(valor) != contq:
        valor = input("digite o valor novamente")
    for x in range(len(valor)):
        final.append(int(valor[x]))
    return final


print(SepararNumeros())
