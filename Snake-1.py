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
cabeza = [[randrange(13), randrange(13)]]

#Función para hacer aparecer la mazana en otra posición
def manzana_posi():
    global manzana
    manzana = [randrange(13), randrange(13)]

#Primera posición de la manzana
manzana_posi()

come = False

while True:
    if cabeza[0] == [55,55]:
        print("Has perdido")
        break
    #Creación de la manzana en el tablero
    r = 0
    while manzana in cabeza:
        manzana_posi()

    #Este for dibuja todo
    for j in range(0, 13):
        for i in range(0, 13):
            if j == cabeza[0][0] and i == cabeza[0][1]:
                print("1", end=" ")
            elif j == manzana[0] and i == manzana[1]:
                print("@", end=" ") 
            elif [j, i] in cabeza[1:]:
                print("0", end=" ") 
            else:
                print("·", end=" ")
        print()

    #Movimiento 
    move = str(input())
    move = move.lower()
    if move == "w":
        cabeza.insert(0,mov.up(cabeza))
        cabeza.pop(-1)
    elif move == "a":
        cabeza.insert(0,mov.left(cabeza))
        cabeza.pop(-1)
    elif move == "s":
        cabeza.insert(0,mov.down(cabeza))
        cabeza.pop(-1)
    elif move == "d":
        cabeza.insert(0,mov.right(cabeza))
        cabeza.pop(-1)
    else:
        cabeza[0] = mov.error()

    if cabeza[0] in cabeza[1:]:
        print("Has perdido")
        break

    if cabeza[0] == manzana:
        manzana_posi()
        cabeza.append(cabeza[-1])

    #Descomentar si se va a usar colab
    #output.clear()
    system("cls")
    