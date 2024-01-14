'''Battleship'''

# Importaciones

import random
#from google.colab import output

#Declaración de variables

filas = 10
columnas = 10
intentos = 0
puntaje = 0

# Función para colocar un barco en el tablero

def colocar_barco(matriz, longitud, etiqueta):

    while True:
        fila = random.randint(1, filas )
        columna = random.randint(1, columnas )
        direccion = random.choice(['horizontal', 'vertical'])

        if direccion == 'horizontal' and columna + longitud <= columnas:
            for i in range(longitud):
                if matriz[fila][columna + i] != 0:
                    break
            else:
                for i in range(longitud):
                    matriz[fila][columna + i] = etiqueta
                break

        elif direccion == 'vertical' and fila + longitud <= filas:
            for i in range(longitud):
                if matriz[fila + i][columna] != 0:
                    break
            else:
                for i in range(longitud):
                    matriz[fila + i][columna] = etiqueta
                break

'''Función que pide las coordenadas y las compara para saber
si es o no un barco'''

def pedir_coordenadas():

    global puntaje
    global intentos

    if intentos < 40 and puntaje < 14:

        print()
        print('Filas (1-10), Columnas (1-10)')
        fila = int(input('Fila: '))
        columna = int(input('Columna: '))

        if fila >= 1 and fila <= 10 and columna >= 1 and columna <= 10:
            while (matriz[fila][columna] == '❎') or \
             (matriz[fila][columna] == '💥'):
                print('Coordenadas repetidas')
                fila = int(input('Fila: '))
                columna = int(input('Columna: '))
            if (matriz[fila][columna] == 0) or (matriz[fila][columna] == '❎'):
                matriz[fila][columna] = '❎'
            else:
                matriz[fila][columna] = '💥'
                puntaje += 1

        else:
            while fila < 1 or fila > 10 or columna < 1 or columna > 10:
                print('Coordenadas no encontradas')
                fila = int(input('Fila: '))
                columna = int(input('Columna: '))
            if (matriz[fila][columna] == 0) or (matriz[fila][columna] == '❎'):
                matriz[fila][columna] = '❎'
            else:
                matriz[fila][columna] = '💥'
                puntaje += 1

# Función que imprime el tablero con los emojis

def imprimir_tablero(matriz):

    print('Bienvenido a Battle Ship')
    print(f'Tienes {40 - intentos} intentos')
    print()
    print('''Son:
- Dos barcos de 2
- Dos barcos de 3
- Un barco de 4''')
    print()

    r = 0
    for renglon in matriz:
        c = 0
        for columna in renglon:
            if matriz[r][c] == '💥':
                print('💥', end='')
            elif matriz[r][c] == '❎':
                print('❎', end='')
            elif isinstance(matriz[r][c], str):
                print(matriz[r][c], end='')
            else:
                print('🔹', end='')
            c += 1
        r += 1
        print()

# Tablero

matriz = [
    ['▪️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'],
    ['1️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['2️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['3️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['4️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['5️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['6️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['7️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['8️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['9️⃣', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['🔟', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Se colocan los barcos

a = colocar_barco(matriz, 2, 1)
b = colocar_barco(matriz, 2, 2)
c = colocar_barco(matriz, 3, 3)
d = colocar_barco(matriz, 3, 4)
e = colocar_barco(matriz, 4, 5)

# Función principal

def main():

    global intentos
    global puntaje
    global matriz

    while intentos <= 40 and puntaje < 14:
        #output.clear()
        imprimir_tablero(matriz)
        pedir_coordenadas()
        intentos += 1

    if puntaje == 14 and intentos < 41:
        #output.clear()
        imprimir_tablero(matriz)
        print()
        print('Ganaste!!!')
        print(f'Terminaste en {intentos} intentos')

    elif puntaje < 14:
        print()
        print('Buen intento!!')
        print(f'Terminaste en {intentos} intentos')

main()