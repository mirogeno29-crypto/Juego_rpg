import personajes

def creacion_mi_personaje():
    mi_personaje = personajes.personaje(input("ingresa tu nombre: "),4,10,1)
    return mi_personaje


personajes_creados = {
"lobo_fuego" : personajes.personaje("Lobo fuego",4,10,1),
"oso_electrico" : personajes.personaje("oso electrico",5,12,2),
"nicolas_maduro" : personajes.personaje("nicolas maduro",6,14,3),}


def arranque_juego():
    personajes_creados["mi_personaje"] = creacion_mi_personaje()
    sala1()
    

def direncion(sala_derecha,sala_izquierda):
    elegir_direccion = int(input("""te encuentras en una cueva con solo dos puertas una a la derecha y otra a la izquierda
    1. ir a la derecha
    2. ir a la izquierda"""))
    
    if elegir_direccion == 1:
        sala_derecha()
    elif elegir_direccion == 2:
        sala_izquierda()
    

def sala0():
     if personajes_creados["mi_personaje"].inventario["pepitas de oro"] == 3:
         print("has ganado el juego")
     else:
         print("necesitas 3 pepitas de oro para abrir esta puerta")
    
#salas llenas    
def sala1():
 print("estas en sala 1")
 
 if direncion() == 1:
     sala2()
 elif direncion() == 2:
     sala0()
    
     
         
     
def sala2():
    print("estas en sala 2")
    a =0
    a +=1
    if a <=2:
     print("un lobo de fuego te ataca")    
     personajes.pelea(personajes_creados["mi_personaje"],personajes_creados["lobo_fuego"])
     personajes_creados["mi_personaje"].inventario["pepitas de oro"]
     print("has obtenido una pepita de oro")
     print("has ganado la batalla")

"""
def sala3():

def sala4():

#salas vacias
def sala2_vacia():

def sala3_vacia():

def sala4_vacia():
"""