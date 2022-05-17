def function(valor, string):
    achou = False
    for x in string:
        if achou == x:
            achou = True
    return achou


print(function("casa", [1.2, 2, 30, 4, "casa"]))
