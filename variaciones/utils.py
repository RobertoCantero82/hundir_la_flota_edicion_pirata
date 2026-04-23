# IMPORTO LAS LIBRERÍAS NECESARIAS

import random # librería para los barcos aleatorios y los disparos aleatorios
import clases # librería con las clases de barcos
import numpy as np # librería para gestionar matrices y arrays

# FUNCIÓN PARA CREAR TABLEROS DE 10X10 CON " " EN CADA CASILLA

def crear_tablero(tamaño:tuple = (10,10)): 
   tablero = np.full(tamaño, " ") # creo un array de tamaño por defecto 10x10
   return tablero # devuelvo el tablero

# FUNCIÓN PARA MOSTRAR LOS TABLEROS EN TERMINAL

def mostrar_tableros(mi_tablero, tablero_rival):  # ← eliminada la línea duplicada de dentro
   header = "   " + " ".join(str(i) for i in range(10)) # Crea "   0 1 2 3 4 5 6 7 8 9"
   
   print("\n" + " " * 10 + "MI TABLERO")
   print(header)
   for i, fila in enumerate(mi_tablero):
      print(f"{i:2} | {' '.join(fila)} |") # El :2 asegura que el número ocupe dos espacios
   
   print("\n" + " " * 8 + "TABLERO RIVAL")
   print(header)
   for i, fila in enumerate(tablero_rival):
      print(f"{i:2} | {' '.join(fila)} |")
   print()

# FUNCIÓN PARA COLOCAR LOS BARCOS EN MI TABLERO (aleatoriamente)

def colocar_barcos(mi_tablero):

   esloras = [2, 2, 2, 3, 3, 4] # creo la lista de esloras
   flota = [] # creo una lista vacía para guardar las posiciones de los barcos

   for i in esloras: # itero por los elementos en la lista de esloras
      barco = clases.Barco(i) # creo el barco de i de eslora
      colocado = False # por defecto el barco se inicia como no colocado

      while not colocado: # repetimos hasta colocarlo sin solapamientos
         f = np.random.randint(0, 10) # fila aleatoria entre 0 y 9
         c = np.random.randint(0, 10) # columna aleatoria entre 0 y 9
         orientacion = random.choice(["H", "V"]) # orientación aleatoria
         provisionales = []

         if orientacion == "H" and c + i <= 10: # compruebo que cabe en horizontal
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f + i <= 10: # compruebo que cabe en vertical
            provisionales = [(fil, c) for fil in range(f, f + i)]

         if provisionales and all(mi_tablero[pos] == " " for pos in provisionales): # si no hay solapamientos
            for pos in provisionales:
               mi_tablero[pos] = "O" # marco la casilla en el tablero
               barco.coordenadas.append(pos) # guardo la coordenada en el barco
            flota.append(barco)
            colocado = True

   return flota # devuelvo la flota para operar en los disparos

# FUNCIÓN PARA COLOCAR LOS BARCOS ALEATORIOS DEL RIVAL

def colocar_barcos_rival(tablero_rival):
   esloras = [2, 2, 2, 3, 3, 4] # creo la lista de esloras
   flota_rival = []  # creo una lista vacía para guardar las posiciones de los barcos del ordenador

   for i in esloras: # itero por los elementos en la lista de esloras
      barco = clases.Barco(i) # creo el barco de i de eslora
      colocado = False # por defecto el barco se inicia como no colocado
   
      while not colocado: # entramos en el bucle principal, que se repetirá hasta que tenga el barco aleatorio colocado
         f = np.random.randint(0,10) # obtengo una fila aleatoria entre 0 y 9
         c = np.random.randint(0,10) # obtengo una columna aleatoria entre 0 y 9
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 10:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f+i <= 10:
            provisionales = [(fil, c) for fil in range(f, f+i)]
         
         if provisionales and all(tablero_rival[pos] == " " for pos in provisionales):
            for pos in provisionales:
               tablero_rival[pos] = "O"
               barco.coordenadas.append(pos)
            flota_rival.append(barco)
            colocado = True
   return flota_rival   

# FUNCIÓN PARA DISPARAR
    
def disparar(casilla, tablero, flota):
   f, c = casilla # se piden fila y columna
   if tablero[f,c] == "O": # si las coordenadas apuntan a una casilla con un "O"
      tablero[f,c] = "X" # la convierto a "X"

      for barco in flota: # se itera la lista de barcos puestos por el jugador
         if casilla in barco.coordenadas: # si las coordenadas del disparo coinciden con las del tablero
            barco.recibir_impacto() # se inicia la función de la clase barco de recibir impacto (quita una vida como atributo)

            if barco.hundido(): # si las vidas llegan a cero
               print(f"¡El {barco.nombre} está hundido!") # se imprime hundido
            else:
               print("¡Tocado!") # si quedan vidas, se imprime tocado

      return "tocado" # hay coincidencia de coordenadas
   
   elif tablero[f,c] == " ": # en caso de que se dispare a una casilla en blanco
      tablero[f,c] = "A" # se cambia su valor por una A
      print("¡Agua!") # se imprime el mensaje
      return "agua" # se devuelve agua
   
   else:
      print("Ya habías disparado aquí") # si el disparo se hace a una casilla diferente de "0" o  de " ", es que
                                        # ya se había disparado. Con lo que hay que repetir y se imprime el mensaje
      return "repetido" # devuelve el repetido