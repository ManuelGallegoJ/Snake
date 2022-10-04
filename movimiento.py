#O(1) (está indexando un deque en la primera posición que es O(1) y luego en esa posición que es un array indexa en la primera o segunda posición O(1)) 


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

