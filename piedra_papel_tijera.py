import random

for i in range(10):
    player=int(input("Elige 1 para piedra, 2 para papel o 3 para tijera: "))
    computer=random.randint(1,3)
    
    if computer==1:
        print("La computadora eligió piedra.")
    elif computer==2:
        print("La computadora eligió papel.")
    else:
        print("La computadora eligió tijera.")

    if player==computer:
        print("Empate")
    elif (player==1 and computer==3) or (player==2 and computer==1) or (player==3 and computer==2):
        print("Ganaste")
    else:
        print("Perdiste")
