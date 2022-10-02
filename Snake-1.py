from os import system
import movimiento as mov
from random import randrange
from collections import deque


"""
NOTA

▲ : Es la cabeza de la serpiente
0 : Es el cuerpo de la serpiente
@ : Es la manzana
X : Es la cabeza cuando la entrada es invalida y el juego se pausa hasta ingresar una tecla valida
"""

#Creación de la serpiente
serpiente = deque([(6, 6),(7,6),(8,6)])  #cola con las ubicaciones de la serpiente en pantalla, se usa pila porque siempre se elimina la cola y se añade una cabeza 

#Función para hacer aparecer la mazana en otra posición
def manzana_posi():
    global manzana
    manzana = (randrange(13), randrange(13))

#Inicializo variables
manzana = (3,9)  #posicion de la manzana en el tablero
creci = False  #variable que determina si la serpiente va a crecer o no
cont_mov = 0  #variable aleatoria que determina cuantos movimientos se han realizado a partir de la ultima manzana comida
move = "w" #variable de entrada que determina en que direccion se mueve la serpiente
ran_pos=-1 #variable aleatoria, inicialmente -1 para no afectar el programa, que determina en cuantos movimientos se generará la proxima manzana

while True: #ciclo de todo el juego, para en cuanto se choca con una pared o con su propio cuerpo

    #la unica forma de que serpiente tenga un false es si las funciones de movimiento determinan que el movimiento se sale del tablero
    if serpiente[0] == False:
        print("Has perdido")
        break

    #verifica si ya se cumplieron los movimientos para que salga una nueva manzana
    if ran_pos==cont_mov:
        manzana_posi()
        cont_mov = 0
        ran_pos=-1  #la variable vuelve a valer -1 para que no salgan mas manzanas

    #si la manzana se crea en el espacio de la serpiente, entonces la vuelve a generar hasta que funcione
    while manzana in serpiente:
        manzana_posi()

    #Este for dibuja todo
    for j in range(0, 13):
        for i in range(0, 13):
            if j == serpiente[0][0] and i == serpiente[0][1]: #verifica si una posicion es la cabeza de la serpiente y le da un icono segun la direccion de la misma
                if move == "w":
                    print("▲", end=" ")
                elif move == "a":
                    print("◄", end=" ")
                elif move == "d":
                    print("►", end=" ")
                elif move == "s":
                    print("▼", end=" ")
                else:
                    print("X", end=" ")
            elif j == manzana[0] and i == manzana[1]: #verifica si una posicion es la posicion de la manzana y la dibuja en pantalla
                print("@", end=" ") 
            elif (j, i) in serpiente: #verifica si una posicion es el cuerpo de la serpiente y la dibuja en pantalla
                print("0", end=" ") 
            else: #si una posicion está libre, entonces se dibuja como un punto
                print("·", end=" ")
        print()

    print('w: Arriba  s: Abajo  a: Izquierda  d: Derecha.') #imprime las instrucciones


    #Movimiento 
    d = True
    moveA = move
    while d:
        move = str(input()).lower() #si el input es en mayuscula lo pone en minuscula

        #los siguientes condicionales verifican en que direccion se debe mover la serpiente
        #para saber que elemento se debe agregar se llama a una funcion de movimiento segun corresponda
        #inserta el nuevo elemento en la cabeza de la serpiente
        #si la serpiente no debe crecer entonces elimina la cola, de lo contrario deja la cola intacta
        #finalmente la variable de crecimiento se pone false para no dar error
        q =(move == "w" and moveA != "s")
        w = (move == "d" and moveA != "a")
        e = (move == "s" and moveA != "w")
        r = (move == "a" and moveA != "d")
        if q or w or e or r:
            d = False
            if move == "w":
                serpiente.insert(0,mov.up(serpiente))
                if creci==False:
                    serpiente.pop()
                creci=False
                cont_mov += 1 #cada moviminto suma uno a esta variable, esto con el fin de saber en que movimiento debe salir una manzana
        
            elif move == "a":
                serpiente.insert(0,mov.left(serpiente))
                if creci==False:
                    serpiente.pop()
                creci=False
                cont_mov += 1 #cada moviminto suma uno a esta variable, esto con el fin de saber en que movimiento debe salir una manzana

            elif move == "s":
                serpiente.insert(0,mov.down(serpiente))
                if creci==False:
                    serpiente.pop()
                creci=False
                cont_mov += 1 #cada moviminto suma uno a esta variable, esto con el fin de saber en que movimiento debe salir una manzana

            elif move == "d":
                serpiente.insert(0,mov.right(serpiente))
                if creci==False:
                    serpiente.pop()
                creci=False
                cont_mov += 1 #cada moviminto suma uno a esta variable, esto con el fin de saber en que movimiento debe salir una manzana



    #Este if verifica si el elemento de la cabeza se repite, es decir si la cabeza choca con el cuerpo, en ese caso el juego termina
    if serpiente.count(serpiente[0])>1:
        system("cls")
        print("Has perdido")
        break

    #Verifica si la cabeza de la erpiente esta en la misma posicion que la manzana, esto indica que se la comió
    if serpiente[0] == manzana:
        cont_mov = 0 #se reinicia el contador de movimientos porque debe empezar a contar desde ahora
        creci=True #Indica que la serpiente debe crecer
        manzana = (-1, -1) #Indica que no hay manzana
        ran_pos = randrange(9)+1 #aqui se asigna aleatoriamente en cuantos movimientos debe aparecer una nueva manzana

    system("cls") #limpia la pantalla en cada movimiento
    