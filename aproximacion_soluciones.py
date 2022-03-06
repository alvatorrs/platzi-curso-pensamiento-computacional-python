'''Calcula la raíz cuadrada de un número de manera aproximada
a traves de una incertidumbre epsilon'''

def main():
    objetivo = int(input("Digite un número: "))
    epsilon = 0.01
    paso = epsilon**2
    
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontro la raiz cuadrada de {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")



if __name__ == "__main__":
    main()