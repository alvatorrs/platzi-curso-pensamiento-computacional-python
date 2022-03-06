
def divide_elementos_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        divisor = int(input('Ingresa un divisor distinto de cero: '))
        return divide_elementos_lista(lista, divisor)


lista = list(range(10))
divisor = 0

nueva_lista = divide_elementos_lista(lista, divisor)
print(nueva_lista)