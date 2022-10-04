#O(1) (está indexando un deque en la primera posición que es O(1) y luego en esa posición que es un array indexa en la primera o segunda posición O(1)) 


#Las siguientes funciones determinan el movimiento de la sepiente según la dirección ingresada
#Además verifican si un movimiento hace que la serpiente se salga del tablero, en este caso devuelve un false que el programa principal identifica como que perdió
#En caso contrario retorna la nueva cabeza de la serpiente, segun a donde se mueva
def up(t):
    if t[0][0]-1 < 0:
        return False
    return (t[0][0]-1, t[0][1])

def left(t):
    if t[0][1]-1 < 0:
        return False
    return (t[0][0], t[0][1]-1)

def down(t):
    if t[0][0]+1 > 12:
        return False
    return (t[0][0]+1, t[0][1])

def right(t):
    if t[0][1]+1 > 12:
        return False
    return (t[0][0], t[0][1]+1)

