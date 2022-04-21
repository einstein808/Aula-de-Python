ano = int(input("digite ano do veiculo."))
peso = int(input("digite peso do veiculo"))
clas1 = 16.50
clas2 = 25.50
clas3 = 46.50
clas4 = 27.00
clas5 = 30.50
clas6 = 52.50
clas7 =19.50
clas8= 55.50
if ano<=1970:
    if peso<1200:
        print(f"A taxa de registro do seu veiculo é: {clas1} ")
    if peso >1200 and peso<=1700:
        print(f"A taxa de registro do seu veiculo é: {clas2} ")
    if peso>1700:
        print(f"A taxa de registro do seu veiculo é: {clas3}")

if ano >=1971 and ano<=1979:
    if peso > 1200:
        print(f"A taxa de registro do seu veiculo é: {clas4} ")
    if peso >=1200 and peso<=1700:
        print(f"A taxa de registro do seu veiculo é: {clas5}")
    if peso > 1700:
        print(f"A taxa de registro do seu veiculo é: {clas6 } ")

if ano>=1980:
    if peso<1600:
        print(f"A taxa de registro do seu veiculo é: {clas7} ")
    else:
        print(f"A taxa de registro do seu veiculo é:  {clas8}")

