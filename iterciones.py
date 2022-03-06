def main():
    
    contador_externo = 0
    contador_interno = 0

    while contador_externo < 5:
        while contador_interno < 10:
            print(contador_externo,contador_interno)
            contador_interno += 1

            if contador_interno >= 3:
                break
        contador_externo += 1
        contador_interno = 0



if __name__ == '__main__':
    main()


'''Cronometro'''
# horas = 0
# minutos = 0

# while horas<24:
#   while minutos<60:
#     print(horas,':',minutos)
#     minutos += 1

#   horas += 1
#   minutos = 0

'''Reloj'''
# horas = 0
# minutos = 0
# segundos = 0

# while horas < 24:
#     while minutos < 60:
#         while segundos < 60:
#             print(f'{horas}:{minutos}:{segundos}') 
#             segundos += 1
#         minutos += 1
#         segundos = 0
#     horas += 1
#     minutos = 0