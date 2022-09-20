def up(t):
    return [t[0]-1, t[1]]

def left(t):
    return [t[0], t[1]-1]

def down(t):
    return [t[0]+1, t[1]]

def right(t):
    return [t[0], t[1]+1]

def error():
    print("Error")
