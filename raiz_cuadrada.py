"""Programa para calcular la raiz cuadrada de un número
    por distintas metodologías"""

def enumeracion_exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene raiz cuadrada exacta")


def aproximacion_soluciones(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontro la raiz cuadrada de {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")


def busqueda_binaria(objetivo):
    epsilon = 0.005
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2
    
    print(f"La raiz cuarada de {objetivo} es {respuesta}")


def main():
    print('Bienvenido a la calculadora de raices cuadradas')
    objetivo = int(input('Ingrese el número a calcular: '))
    print('Selecciones uno de los siguientes métodos: ')
    print("""
     [1] Enumeración exhaustiva
     [2] Aproximación de soluciones
     [3] Busqueda binaria
    """)
    opcion = int(input('Opción: '))

    if opcion == 1:
        enumeracion_exhaustiva(objetivo)
    elif opcion == 2:
        aproximacion_soluciones(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print('Intentelo de nuevo :)')


if __name__ == '__main__':
    main()