def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

resultado = division(10, 2)
if resultado == 5:
    print("Prueba exitosa")
else:
    print("Prueba fallida")

resultado = division(10, 0)
if resultado == 1:
    print("Prueba exitosa")
else:
    print("Prueba fallida")
    