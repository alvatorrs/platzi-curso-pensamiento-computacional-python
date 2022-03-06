''' Calcular la raíz cuadrada exacta de un número 
por el método de enumeración exhaustiva'''

def main():
    objetivo = int(input("Digite un número: "))

    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene raiz cuadrada exacta")


if __name__ == "__main__":
    main()