# Comparador de edades

def main():
    print('''//Bienvenido al comparador de edades 
por favor introdusca los siguientes datos//''')
    name1 = input('Cuál es el primer nombre: ')
    name1_age = int(input('Edad: '))
    name2 = input('Cuál es el segundo nombre: ')
    name2_age = int(input('Edad: '))

    

    if name1_age > name2_age:
        diferencia = name1_age - name2_age
        print(f'{name1} es mayor que {name2} por {diferencia} años')
    elif name1_age < name2_age:
        diferencia = name2_age - name1_age
        print(f'{name2} es mayor que {name1} por {diferencia} años')
    else:
        print(f'Tanto {name1} como {name2} tienen la misma edad')


if __name__ == '__main__':
    main()