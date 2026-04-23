# IMPORTO LAS LIBRERÍAS y CÓDIGOS DE COLOR

import random # librería para los barcos aleatorios y los disparos aleatorios
import clasesprueba # ← corregido: antes ponía "clases"
import numpy as np # librería para gestionar matrices y arrays

ROJO    = "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"

# FUNCIÓN PARA CREAR TABLEROS 

def crear_tablero(tamaño:tuple = (3,3)):
   tablero = np.full(tamaño, " ")
   return tablero

# FUNCIÓN PARA COLOREAR CELDAS

def colorear_celda(celda):
    if celda == "X":
        return f"{ROJO}X{RESET}"
    elif celda == "A":
        return f"{AZUL}A{RESET}"
    return celda

# FUNCIÓN PARA MOSTRAR LOS TABLEROS EN TERMINAL

def mostrar_tableros(mi_tablero, tablero_rival):
   header = "     " + " ".join(str(i) for i in range(3))
   
   print("\n" "     TABLERO")
   print("DEL SUCIO JUGADOR")
   print()
   print(header)
   for i, fila in enumerate(mi_tablero):
      fila_coloreada = " ".join(colorear_celda(c) for c in fila)
      print(f"{i:2} | {fila_coloreada} |")
   print()
   
   print("     TABLERO")
   print("DEL APUESTO PIRATA")
   print()
   print(header)
   for i, fila in enumerate(tablero_rival):
      fila_coloreada = " ".join(colorear_celda(c) for c in fila)
      print(f"{i:2} | {fila_coloreada} |")
   print()

# FUNCIÓN PARA COLOCAR MI BARCO (aleatoriamente)

def colocar_barcos(mi_tablero):

   esloras = [2]
   flota = []

   for i in esloras:
      barco = clasesprueba.Barco(i) 
      colocado = False

      while not colocado:
         f = np.random.randint(0, 3)
         c = np.random.randint(0, 3)
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 3:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f + i <= 3:
            provisionales = [(fil, c) for fil in range(f, f + i)]

         if provisionales and all(mi_tablero[pos] == " " for pos in provisionales):
            for pos in provisionales:
               mi_tablero[pos] = "O"
               barco.coordenadas.append(pos)
            flota.append(barco)
            colocado = True

   return flota

# FUNCIÓN PARA COLOCAR EL BARCO ALEATORIO DEL RIVAL

def colocar_barcos_rival(tablero_rival):

   esloras = [2]
   flota_rival = []

   for i in esloras:
      barco = clasesprueba.Barco(i) 
      colocado = False
   
      while not colocado:
         f = np.random.randint(0, 3)
         c = np.random.randint(0, 3)
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 3:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f + i <= 3:
            provisionales = [(fil, c) for fil in range(f, f + i)]
         
         if provisionales and all(tablero_rival[pos] == " " for pos in provisionales):
            for pos in provisionales:
               tablero_rival[pos] = "O"
               barco.coordenadas.append(pos)
            flota_rival.append(barco)
            colocado = True

   return flota_rival

# FUNCIÓN PARA DISPARAR
    
def disparar(casilla, tablero, flota):
   f, c = casilla
   if tablero[f,c] == "O":
      tablero[f,c] = "X"

      for barco in flota:
         if casilla in barco.coordenadas:
            barco.recibir_impacto()

            if barco.hundido():
               print(f"  🏴‍☠️  ¡La {barco.nombre} está hundida!  🏴‍☠️  ")
               print()
            else:
               print(" 🧨 ¡Tocado! 🧨 ")

      return "tocado"
   
   elif tablero[f,c] == " ":
      tablero[f,c] = "A"
      print(" 🌀 ¡Agua!🌀")
      return "agua"
   
   else:
      print(" 🙄 ¡Inútil! Ya has malgastado pólvora en esa zona. ¿Acaso intentas pescar? 🙄 ")
      print()
      return "repetido"