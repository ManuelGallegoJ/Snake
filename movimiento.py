def up(t):
    if t[0]-1 < 0:
        return [55,55]
    return [t[0]-1, t[1]]

def left(t):
    if t[1]-1 < 0:
        return [55,55]
    return [t[0], t[1]-1]

def down(t):
    if t[0]+1 > 12:
        return [55,55]
    return [t[0]+1, t[1]]

def right(t):
    if t[1]+1 > 12:
        return [55,55]
    return [t[0], t[1]+1]

def error():
    print("Error.")
