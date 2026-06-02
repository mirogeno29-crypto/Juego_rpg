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
    

def direncion():
    elegir_direccion = input(int("""te encuentras en una cueva con solo dos puertas una a la derecha y otra a la izquierda
    1. ir a la derecha
    2. ir a la izquierda"""))
    
    return elegir_direccion
    
#salas llenas    
def sala1():
 print("estas en sala 1")
 if direncion() == 1:
     if personajes_creados["mi_personaje"].inventario["pepitas de oro"] == 3:
         print("has ganado ")
         
     
 

def sala2():

def sala3():

def sala4():

#salas vacias
def sala2_vacia():

def sala3_vacia():

def sala4_vacia():
