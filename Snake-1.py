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

#Creación de la serpiente
cabeza = [randrange(13), randrange(13)]

#Función para hacer aparecer la mazana en otra posición
def manzana_posi():
    global manzana
    manzana = [randrange(13), randrange(13)]

#Primera posición de la manzana
manzana_posi()

while True:
    if cabeza == [55,55]:
        print("Has perdido")
        break
    #Creación de la manzana en el tablero
    r = 0
    while manzana == cabeza:
        r += 1
        manzana_posi()
        print(manzana, r)

    #Este for dibuja todo
    for j in range(0, 13):
        for i in range(0, 13):
            if j == cabeza[0] and i == cabeza[1]:
                print("1", end=" ")
            elif j == manzana[0] and i == manzana[1]:
                print("@", end=" ") 
            else:
                print("·", end=" ")
        print()

    #Movimiento 
    move = str(input())
    move = move.lower()
    if move == "w":
        cabeza = mov.up(cabeza)
    elif move == "a":
        cabeza = mov.left(cabeza)
    elif move == "s":
        cabeza = mov.down(cabeza)
    elif move == "d":
        cabeza = mov.right(cabeza)
    else:
        cabeza = mov.error()

    #Descomentar si se va a usar colab
    #output.clear()
    system("cls")