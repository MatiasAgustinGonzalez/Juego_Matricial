import time 

FILAS = int(input("Ingrese la canidad de filas que desea ver en la matriz: "))
COLUMNAS = int(input("Ingrese la canidad de columnas que desea ver en la matriz: "))

def dibujar_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)
    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    for xx in tablero:
        print("  ".join(xx))

def mover(posicion_fila, posicion_columna):
    posicion_fila += 1
    posicion_columna += 1
    if posicion_fila > FILAS - 1:
        posicion_fila = 0
    if posicion_columna > COLUMNAS - 1:
        posicion_columna = 0
    return posicion_fila, posicion_columna

posicion_fila = 0
posicion_columna = 0
while True:
    posicion_fila, posicion_columna = mover(posicion_fila, posicion_columna)
    dibujar_tablero(posicion_fila, posicion_columna)
    print()
    time.sleep(0.5)