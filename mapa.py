import sys
import personajes
import random


def eligir_direccion():
    direcion = int(input("""Te encuentras en una cueva con dos puertas, una a la derecha y otra a la izquierda.
Elige cuál quieres abrir.
                     
    1.izquierda
    2.derecha             
    3.ver estadisticas
    4.revisar inventario             
                     
                     """))
    
    return direcion




def sala0():
    if personajes.mi_personaje.inventario["pepitas de oro"] ==3:
        print("Has ganado el juego")
    elif personajes.mi_personaje.inventario["pepitas de oro"] < 3:
        print("Necesitas 3 pepitas de oro para abrir esta puerta\n")
        sala1()

def sala1():
     direcion = eligir_direccion()
     if direcion == 1:
      sala0()
     elif direcion == 2:
      sala2()
     elif direcion == 3:
         personajes.mi_personaje.Mostrar_atributos()
         sala1()
     elif direcion == 4:
         personajes.mi_personaje.usar_inventario()
         sala1()
        
def sala2():
    global sala1
    sala1 = sala1_vacia
    global pepitas_oro
    print("un lobo de fuego te ataca")
    #futura funcion de pelea con lobo de fuego si pierdo se acaba el programa
    personajes.pelea(personajes.mi_personaje,personajes.lobo_fuego)
    personajes.mi_personaje.subir_nivel()
    print("has subido de nivel")
    print("has obtenido una pepita de oro")
    print("has obtenido una posion de vida")
    personajes.mi_personaje.inventario["pepitas de oro"] += 1
    personajes.mi_personaje.inventario["posion vida"] += 1
    global sala2
    sala2 = sala2_vacia
    sala2()
    

        
def sala3():
    print("un oso electrico te ataca")
    #futura funcion de pelea con oso electrico si pierdo se acaba el programa
    personajes.pelea(personajes.mi_personaje,personajes.oso_electrico)
    personajes.mi_personaje.subir_nivel()
    print("has subido de nivel")
    print("has obtenifo una pepita de oro")
    print("has obtenido una posion de vida")
    personajes.mi_personaje.inventario["pepitas de oro"] += 1
    personajes.mi_personaje.inventario["posion vida"] += 1
    global sala3
    sala3 = sala3_vacia
    sala3()
    

        
def sala4():
    print("nicolas maduro te ataca")
    #futura funcion de pelea con nicolas maduro si pierdo se acaba el programa
    personajes.pelea(personajes.mi_personaje,personajes.nicolas_maduro)
    personajes.mi_personaje.subir_nivel()
    print("has subido de nivel")
    print("has obtenido una pepita de oro")
    print("has obtenido una posicion de vida")
    personajes.mi_personaje.inventario["pepitas de oro"] += 1
    personajes.mi_personaje.inventario["posion vida"] += 1
    if random.random() >0.5:
        personajes.mi_personaje.inventario["cenizas de chavez"] =1
        print("has obtenido las cenizas de chavez")
    global sala4
    sala4 = sala4_vacia
    sala4()
    
# SALAS VACIAS    


def sala1_vacia():
     print("Estas en sala 1\n")
     direcion = eligir_direccion()
     if direcion == 1:
      sala0()
     elif direcion == 2:
      sala2()
     elif direcion == 3:
         personajes.mi_personaje.Mostrar_atributos()
         sala1_vacia()
     elif direcion == 4:
         personajes.mi_personaje.usar_inventario()
         sala1_vacia()
    
    
def sala2_vacia():
    print("Estas en sala 2\n")
    direcion = eligir_direccion()
    if direcion == 1:
        sala1()
    elif direcion == 2:
        sala3()   
    elif direcion == 3:
         personajes.mi_personaje.Mostrar_atributos()
         sala2_vacia()
    elif direcion == 4:
         personajes.mi_personaje.usar_inventario()
         sala2_vacia()
                
def sala3_vacia():
    print("Estas en sala 3\n")
    direcion = eligir_direccion()
    if direcion == 1:
        sala2_vacia()
    elif direcion == 2:
         print("Entras a sala 4")
         sala4()
    elif direcion == 3:
         personajes.mi_personaje.Mostrar_atributos()
         sala3_vacia()
    elif direcion == 4:
         personajes.mi_personaje.usar_inventario()
         sala3_vacia()
            
def sala4_vacia():
    direcion = int(input("""Solo está la puerta de la izquierda. ¿Quieres entrar en ella?

1.Sí
2.No\n"""))
    if direcion == 1:
        sala3_vacia()
    elif direcion == 2:
        sala4_vacia()
    elif direcion == 3:
         personajes.mi_personaje.Mostrar_atributos()
         sala4_vacia()
    
    
    
    
            
    
     
     
     
