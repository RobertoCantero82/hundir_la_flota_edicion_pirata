# IMPORTAR LIBRERÍAS

import clases
import utils
import time
import random
import numpy as np

# CREAR LOS TABLEROS

mi_tablero = utils.crear_tablero()           
tablero_rival = utils.crear_tablero()        
tablero_rival_oculto = utils.crear_tablero() 

print("  🏴‍☠️  ¡Bienvenido a Hundir la Flota! -- VERSIÓN PIRATA (Patrocinado por The Secret Of Monkey Island)  🏴‍☠️  ")
print()
time.sleep(2)

# COLOCAMOS LOS BARCOS

print(" ⛵ Desplegando tu flota...aspirante... ⛵ ")
time.sleep(2)
flota = utils.colocar_barcos(mi_tablero)
print()
print(" 🍺 ¡Mi flota ya está desplegada! (Y sin derramar ni una gota de grog...) 🍺 ")
time.sleep(2)
print()
print("  🌫️  Escondiendo mis barcos entre la niebla...  🌫️  ")
time.sleep(2)
flota_rival = utils.colocar_barcos_rival(tablero_rival_oculto)
print()
print("  ⚔️  ¡Listos para la batalla! (y para los insultos)  ⚔️  ")
time.sleep(2)

# BUCLE DE JUEGO

jugador_gana = False
rival_gana = False
rendido = False
disparo = None

while not jugador_gana and not rival_gana:

    print()
    print("≈" * 50)
    print()
    time.sleep(1)  
    utils.mostrar_tableros(mi_tablero, tablero_rival)

    # Turno del jugador

    try:
        accion = input(" 💣 ¡Dispara el cañón! (Fila Columna) o 'Q' para huir como un pollo 🐔 : ").lower()
        print()

        if accion == 'q': # si abandono, mensaje de despedida
            mensajes_rendicion = [
                " 🐒🐒🐒 ¿Te rindes? ¡Mira, detrás de ti, un mono de tres cabezas! 🐒🐒🐒 ",
                " 👎 ¿Abandonas?... ¡Sabía que ese traje de pirata te venía grande! 👎 ",
                " 🗣️ ¿Rendido? ¡Vuelve cuando hayas aprendido a insultar como un pirata! 🗣️ ",
                " 💀 Error 404: valentía no encontrada. Regresa cuando tengas agallas. 💀 "
            ]
            print(random.choice(mensajes_rendicion))
            print()
            rendido = True
            break

        coords = accion.replace(",", " ").split()
        if len(coords) != 2: # si escribo mal los números, error
            print(" 🤕 ¡Casi te cortas con tu propio garfio! El formato es: 1 2 🤕 ")
            print()
            continue

        f, c = map(int, coords)

        if not (0 <= f <= 9 and 0 <= c <= 9): # si pongo un rango fuera del tablero, error
            print(" 📜 ¡Te sales del mapa! Tu mundo solo está entre el 0 y el 9. 📜 ")
            print()
            continue

        disparo = utils.disparar((f, c), tablero_rival_oculto, flota_rival)
        time.sleep(1)
        print()

        if disparo == "tocado":
            tablero_rival[f, c] = "X"
            jugador_gana = not np.any(tablero_rival_oculto == "O")
            if jugador_gana:
                time.sleep(1)
                break
            print(" ✨ ¡Me has dado! ¡Luchas como un auténtico pirata! ✨ ")
            print()
            time.sleep(1)
            continue
        elif disparo == "agua":
            tablero_rival[f, c] = "A"
            time.sleep(1)

    except ValueError: # mensaje de error cuando no se utilizan números
        print(" 🔢 ¡Eso no son coordenadas, son insultos mal redactados! ¡Usa números! 🔢 ")
        print()
        continue

    #  Turno del rival 

    if disparo != "repetido":
        print(" 🧭 Estoy consultando la brújula... ¡Prepárate! 🧭 ")
        print()
        time.sleep(1)

        f_aleatoria = np.random.randint(0, 10)  
        c_aleatoria = np.random.randint(0, 10)

        print(f" ☄️ ¡Un proyectil silba hacia ({f_aleatoria}, {c_aleatoria})")
        print()
        time.sleep(1)

        disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)
        time.sleep(1)
        print()  

        rival_gana = not np.any(mi_tablero == "O")  # compruebo victoria rival tras primer disparo
        
        while disparo_rival == "tocado" and not rival_gana: 
            print(" 🆘 ¡Te he dado! ¡Tu apellido ahora es Problemas! 🆘 ")
            print()
            time.sleep(1)

            f_aleatoria = np.random.randint(0, 10)  
            c_aleatoria = np.random.randint(0, 10)
            print(f" 🚨 ¡Otro de mis cañonazos vuela hacia ({f_aleatoria}, {c_aleatoria})! 🚨 ")
            time.sleep(1)
            print()

            disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)
            time.sleep(1)
            print()

            rival_gana = not np.any(mi_tablero == "O")  # compruebo victoria rival tras cada disparo extra
   
    # Compruebo si hay victoria

    jugador_gana = not np.any(tablero_rival_oculto == "O")
    rival_gana = not np.any(mi_tablero == "O")
    time.sleep(1)

# RESULTADO

if not rendido:
    print()
    print("≈" * 50)
    print()
    time.sleep(1)
    utils.mostrar_tableros(mi_tablero, tablero_rival)
    time.sleep(1)
    print()

    if jugador_gana:
        mensajes_victoria = [
            " 🐄 ¡Has ganado! Claramente mi flota lucha como una vaca. 🐄 ",
            " 🏆 ¿¡Como?! Has hundido mis barcos más rápido que el grog en la garganta de un pirata. 🏆 ",
            " 🗡️ ¡Nooooo! Tus disparos son más afilados que mi espada (que por cierto, está recién afilada). 🗡️ "
        ]
        print(random.choice(mensajes_victoria))
    elif rival_gana:
        mensajes_derrota = [
            " 🦀 ¡He hundido tu flota! Espero que te guste el fondo del mar, aunque no hay mucho grog. 🦀 ",
            " 😎 ¡He ganado! Al menos ahora tus barcos no tendrán que aguantar tu cara. 😎 ",
            " 🧐 ¡Hundido! Mis disparos son tan certeros como mi dialéctica. 🧐 "
        ]
        print(random.choice(mensajes_derrota))
    print()