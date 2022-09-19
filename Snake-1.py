from os import system
#Descomentar si se va a usar colab
#from google.colab import output

tablero = []
for k in range(0, 13):
  tablero.append(["·" for i in range(0,13)])  
while True:
  for j in range(0, 13):
    for i in range(0, 13):
      print(tablero[j][i], end=" ")
    print()


  if input() == "y":
    break  
#Descomentar si se va a usar colab
  #output.clear()
  system("cls")