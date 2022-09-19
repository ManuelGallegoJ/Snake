from os import system
import movimiento as mov
from random import randrange

#Descomentar si se va a usar colab
#from google.colab import output

"""
NOTA

1 : Es la cabeza de la serpiente
0 : Es el cuerpo de la serpiente
@ : Es la manzana
"""

#Creación del tablero
tablero = []
for k in range(0, 13):
    tablero.append(["·" for i in range(0,13)])  
    
#Creación de la serpiente
cabeza = [randrange(13), randrange(13)]
tablero[cabeza[0]][cabeza[1]] = "1"

#Función para hacer aparecer la mazana en otra posición
def manzana_posi():
    global manzana
    manzana = [randrange(13), randrange(13)]

#Primera posición de la manzana
manzana_posi()

while True:

    #Creación de la manzana en el tablero
    r = 0
    while manzana == cabeza or """manzana is in cuerpo""" :
        r += 1
        manzana_posi()
        print(manzana, r)
    tablero[manzana[0]][manzana[1]] = "@"

    #Este for dibuja todo
    for j in range(0, 13):
        for i in range(0, 13):
            print(tablero[j][i], end=" ")
        print()

    #Movimiento 
    move = str(input())
    move = move.lower()
    if move == "w":
        mov.up(tablero)
    elif move == "a":
        mov.left(tablero)
    elif move == "s":
        mov.down(tablero)
    elif move == "d":
        mov.right(tablero)
    else:
        mov.error()

    #Descomentar si se va a usar colab
    #output.clear()
    system("cls")