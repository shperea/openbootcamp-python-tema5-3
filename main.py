def es_bisiesto(year):
    return year % 4

year = int(input("Escribe un año: "))
resultado = es_bisiesto(year)

if resultado == 0:
    print("El año", year, "es bisiesto")
else:
    print("El año", year, "no es bisiesto")