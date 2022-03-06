'''Encontrar el calculo de una raiz cuadrada por el metodo
de busqueda binaria'''

def main():
    objetivo = int(input("Digite un número: "))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2
    
    print(f"La raiz cuarada de {objetivo} es {respuesta}")


if __name__ == "__main__":
    main()