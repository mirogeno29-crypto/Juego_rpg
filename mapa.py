import personajes
import exepciones
import time


def creacion_mi_personaje():
    mi_personaje = personajes.personaje(input("ingresa tu nombre: "),4,10,1)
    return mi_personaje


varibles_salas = {
    
    "sala2": 0,
    "sala3": 0,
    "sala4": 0
    
}


def arranque_juego():
    global lobo_fuego
    global oso_electrico
    global nicolas_maduro
    global mi_personaje
    lobo_fuego = personajes.personaje("Lobo fuego",4,10,1)
    oso_electrico = personajes.personaje("oso electrico",5,12,2)
    nicolas_maduro = personajes.personaje("nicolas maduro",6,14,3)
    mi_personaje = creacion_mi_personaje()
    
    sala1()
    

def direncion(sala_izquierda,sala_derecha):
    while True:
     elegir_direccion = int(input("""te encuentras en una cueva con solo dos puertas una a la derecha y otra a la izquierda
     1. ir a la izquierda
     2. ir a la derecha
     3. usar inventario
     4. ver estadisticas
    
    """))
    
     if elegir_direccion == 1:
        sala_izquierda()
     elif elegir_direccion == 2:
        sala_derecha()
     elif elegir_direccion == 3:
        mi_personaje.usar_inventario()
     elif elegir_direccion == 4:
         mi_personaje.Mostrar_atributos()
    

def sala0():
     if mi_personaje.inventario["pepitas de oro"] == 3:
         print("has ganado el juego")
         time.sleep(4)
         raise exepciones.muertejugador()
         
     else:
         print("necesitas 3 pepitas de oro para abrir esta puerta")
         sala1()
    

def sala1():
 print("estas en sala 1")
 
 direncion(sala0,sala2)
    
        
def sala2():
    print("estas en sala 2")
    varibles_salas["sala2"] +=1
    if varibles_salas["sala2"] <2:
     print("un lobo de fuego te ataca")    
     personajes.pelea(mi_personaje,lobo_fuego)
     mi_personaje.inventario["pepitas de oro"] +=1
     mi_personaje.inventario["posion vida"] +=1
     mi_personaje.subir_nivel()
     print("has subido de nivel")
     print("has obtenido una posion de vida")
     print("has obtenido una pepita de oro")
     direncion(sala1,sala3)
    else:
        direncion(sala1,sala3)


def sala3():
    print("estas en sala 3")
    varibles_salas["sala3"] +=1
    if varibles_salas["sala3"] <2:
     print("un oso lectrico te ataca")    
     personajes.pelea(mi_personaje,oso_electrico)
     mi_personaje.inventario["pepitas de oro"] +=1
     mi_personaje.inventario["posion vida"] +=1
     mi_personaje.subir_nivel()
     print("has subido de nivel")
     print("has obtenido una posion de vida")
     print("has obtenido una pepita de oro")
     direncion(sala2,sala4)
    else:
        direncion(sala2,sala4)

def sala4():
    print("estas en sala 4")
    varibles_salas["sala4"] +=1
    if  varibles_salas["sala4"] <2:
     print("nicolas maduro te ataca")    
     personajes.pelea(mi_personaje,nicolas_maduro)
     mi_personaje.inventario["pepitas de oro"] +=1
     mi_personaje.inventario["posion vida"] +=1
     mi_personaje.subir_nivel()
     print("has subido de nivel")
     print("has obtenido una posion de vida")
     print("has obtenido una pepita de oro")
     while True:
      puerta = int(input("""solo hay una puerta a la izquierda:
    1.entrar 
    2.usar inventario 
    3.ver atributos
    
    """))
      if puerta == 1:
          sala3()
      elif puerta ==2:
          mi_personaje.usar_inventario()
      elif puerta ==3:
          mi_personaje.Mostrar_atributos
          
    else:
      while True:
       puerta = int(input("""solo hay una puerta a la izquierda:
                          1.entrar
                          2.usar inventario
                          3.ver atributos"""))
       if puerta == 1:
          sala3()
       elif puerta ==2:
          mi_personaje.usar_inventario()
       elif puerta ==3:
          mi_personaje.Mostrar_atributos
    