
tempo = int(input("digite tempo que deseja investir em meses"))
if tempo >=5*12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.95% aa")
elif tempo<5*12 and tempo>=4*12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.90% aa")
elif tempo<4*12 and tempo>=3*12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.85% aa")
elif tempo<3*12 and tempo>=2*12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.75% aa")
elif tempo < 2 * 12 and tempo >= 1* 12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.65% aa")
elif tempo<12:
    print(f"investindo em {int(tempo)} meses a taxa de juros é: 0.55% aa")