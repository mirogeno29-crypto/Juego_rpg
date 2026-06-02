

while True:
 jugar = int(input(("""Bienvenido al juego que humilla a GTA 5, Elden Ring y Red Dead Redemption 2, entre otros:

1. Jugar
2. No, gracias\n
""")))
 
 if jugar == 1:
     import mapa
     mapa.sala1()
 elif jugar == 2:
     break