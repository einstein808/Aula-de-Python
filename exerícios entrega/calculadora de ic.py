while True:
    altura = float(input("digite sua altura em metros"))
    if altura > 3 or altura <0.2:
        print(" altura ivalida digite novamente.")
    else:
        break

while True:
    peso = float(input("digite sua peso em kilos"))
    if peso > 400 or peso <5:
        print(" peso ivalido digite novamente.")
    else:
        break
imc = peso / altura**2
if imc >=18.5 and imc<= 24.9:
    print("peso normal")
elif imc >=25 and imc <=29.9:
    print("Sobrepeso")
elif imc >30 and imc <40:
    print("obesidade")
elif imc>40:
    print("obesidade grave")
else:
    print("abaixo do peso")
