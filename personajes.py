import time
import exepciones


#clase de los personajes
class personaje:
    def __init__(self,nombre,ataque,vida_absoluta,defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida_absoluta
        self.vida_absoluta = vida_absoluta
        self.defensa = defensa
        self.inventario = {"pepitas de oro": 0, "posion vida": 0}
    def Mostrar_atributos(self):
        print("ATRIBUTOS: ")
        print(f"nombre: {self.nombre}")
        print(f"ataque: {self.ataque}")
        print(f"vida: {self.vida}")
        print(f"defensa: {self.defensa}")
        
    def usar_inventario(self):
        print(f"inventario: {self.inventario}")
        usar = int(input("""¿Qué quieres usar?

1.Poción de vida
2.Pepita de oro
3.Nada\n """))
        if usar ==1:
         self.usar_posicion_vida()
        if usar ==2:
            print("reune 3 y llevelas a la puerta del final\n")
           
    def atacar(self,enemigo):
        enemigo.vida = enemigo.vida - (self.ataque-self.defensa)
    def morir(self):
        print("Has muerto")
        time.sleep(4)
        raise exepciones.muertejugador()
    def usar_posicion_vida(self):
        if self.inventario["posion vida"]>0:
            print("Te has curado\n")
            self.vida = self.vida_absoluta
            self.inventario["posion vida"] -=1
        else:
            print("no tienes")
    def subir_nivel(self):
        self.ataque +=1
        self.vida_absoluta +=2
        self.defensa +=1
        
        
        




#funcion de pelea

def pelea(peleador_jugador,peleador_npc):
    while True:
     
     peleador_jugador.Mostrar_atributos()
     print("\nhas atacado al enemigo")
     time.sleep(4)
     peleador_jugador.atacar(peleador_npc)
     if  peleador_npc.vida <=0:
         print("\nhas ganado")
         break
     peleador_npc.atacar(peleador_jugador)
     print("\nel enmigo te ha atacado")
     if peleador_jugador.vida <= 0:
       peleador_jugador.morir()
