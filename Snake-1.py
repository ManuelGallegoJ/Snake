from os import system
import movimiento as mov
from random import randrange

#Descomentar si se va a usar colab
#from google.colab import output

"""
NOTA

▲ : Es la cabeza de la serpiente
0 : Es el cuerpo de la serpiente
@ : Es la manzana
"""

#Creación de la serpiente
serpiente = [[6, 6],[7,6],[8,6]]

#Función para hacer aparecer la mazana en otra posición
def manzana_posi():
    global manzana
    manzana = [randrange(13), randrange(13)]

#Inicializo variables
manzana = [3,9]
come = False
creci = 0
cont_com = 0
move = "w"

while True:
    if serpiente[0] == [55,55]:
        print("Has perdido")
        break
    #Creación de la manzana en el tablero
    r = 0
    while manzana in serpiente:
        manzana_posi()

    #Este for dibuja todo
    for j in range(0, 13):
        for i in range(0, 13):
            if j == serpiente[0][0] and i == serpiente[0][1]:
                if move == "w":
                    print("▲", end=" ")
                elif move == "a":
                    print("◄", end=" ")
                elif move == "d":
                    print("►", end=" ")
                else:
                    print("▼", end=" ")
            elif j == manzana[0] and i == manzana[1]:
                print("@", end=" ") 
            elif [j, i] in serpiente[1:]:
                print("0", end=" ") 
            else:
                print("·", end=" ")
        print()

    #Movimiento 
    move = str(input())
    move = move.lower()
    if move == "w":
        serpiente.insert(0,mov.up(serpiente))
        serpiente.pop(-1)
    elif move == "a":
        serpiente.insert(0,mov.left(serpiente))
        serpiente.pop(-1)
    elif move == "s":
        serpiente.insert(0,mov.down(serpiente))
        serpiente.pop(-1)
    elif move == "d":
        serpiente.insert(0,mov.right(serpiente))
        serpiente.pop(-1)
    else:
        serpiente[0] = mov.error()
    cont_com += 1

    #Muere por comerse
    #Carlos se la come
    if serpiente[0] in serpiente[1:]:
        print("Has perdido")
        break

    #Come manzana
    if serpiente[0] == manzana:
        cont_com = 0
        creci +=  1
        manzana = [-1,-1]
        ran_pos = randrange(9)+1
        come = True

    #Se verifica que la manzana aparece x movimientos después
    if come and ran_pos == cont_com:
        manzana_posi()
        come = False
        cont_com = 0

    #Crecimiento
    if creci > 0:
        serpiente.append(serpiente[-1])
        creci -= 1

    #Descomentar si se va a usar colab
    #output.clear()
    system("cls")
