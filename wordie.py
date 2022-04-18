
import os
import random

JUGAR = 1
SALIR = 0


def imprimir_menu():
    os.system('cls')
    print(f'''                                           WORDIE
{JUGAR}) jugar
{SALIR}) Salir
''')


palabras = ['agua', 'canasto', 'auto', 'avion', 'nave',
            'bicicleta', 'torpedo', 'rueda', 'moto', 'pistola', 'bala']


def seleccion_palabra():
    palabra = random.choice(palabras)

    return palabra


def adivina():
    juego = seleccion_palabra()

    guiones = '_'*len(juego)
    global largo
    largo = len(juego)
    contador = 0
    print(
        f'Tenes que adivinar una palabra de {largo} letras y solo tenes {largo} oportunidades para hacerlo')

    input('presiona Enter para continuar')
    s = guiones

    while juego != s and contador < largo:
        a = input(f'nueva palabra de {largo} letras: ')
        if len(a) > largo or len(a) < largo:
            print(f'error, la palabra tiene mas o menos de {largo} letras.')

        else:
            for i in range(largo):
                posicionJuego = juego[i]
                posicionA = a[i]
                if posicionJuego == posicionA:
                    l = list(s)
                    l[i] = posicionJuego
                    s = "".join(l)

            contador += 1
        print(
            f'\n                                                         {s}\n')
        print('intento numero', contador)

    if contador == largo:
        contador = 0
        print('PERDISTE BURRO')

    else:
        if s == juego:
            contador = 0

            print('CORRECTO')
        print(
            f'\n\n                                                              {juego}\n\n')


input('Presiona Enter para continuar...')


def main():
    continuar = True
    while continuar:
        global juego
        os.system('cls')
        imprimir_menu()
        opc = int(input('selecciona opcion: '))
        if opc == JUGAR:
            adivina()
        elif opc == SALIR:
            print('Chau')
            continuar = False
        else:
            print('opcion no valida')
        input('presiona enter para continuar...')


if __name__ == '__main__':
    main()
