import mapa
import exepciones
import time
import os


while True:
 try:
  os.system("cls")   
  print("hola bienvenido a la segunda version del juego mas chafa que te puedas imaginar")
  jugar = int(input("¿quieres jugar? 1.si  2.no: "))
 
  if jugar == 1:
      mapa.arranque_juego()
      
  elif jugar == 2:
      print("entiendo que no quieras ¿quien querria?")
      break
 except exepciones.muertejugador:
      print("reinicio de partida")
      time.sleep(4)