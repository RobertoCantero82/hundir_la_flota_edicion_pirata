# IMPORTAR LIBRERÍAS

import clases
import utils
import time
import random
import numpy as np

# CREAR LOS TABLEROS

mi_tablero = utils.crear_tablero()           # Tablero 3x3 del jugador
tablero_rival = utils.crear_tablero()        # Tablero 3x3 del rival (visible, sin barcos)
tablero_rival_oculto = utils.crear_tablero() # Tablero 3x3 del rival (con barcos ocultos)

print("¡Bienvenido a Hundir la Flota! ⚓ [VERSIÓN PIRATA (Patrocinado por The Secret Of Monkey Island)]")
print()

# COLOCAMOS LOS BARCOS

print("🚢 Desplegando tu flota... ¡Espero que no sea de papel!")
time.sleep(1)
flota = utils.colocar_barcos(mi_tablero)
print("🤖 Preparando los barcos... ¡Detrás de ti, un mono de tres cabezas!")
time.sleep(1)
flota_rival = utils.colocar_barcos_rival(tablero_rival_oculto)
print("¡Luchemos!")

# BUCLE DE JUEGO

print("¡Empieza el juego!")

jugador_gana = False
rival_gana = False
rendido = False
disparo = None

while not jugador_gana and not rival_gana:

    print("─" * 25)  # ← separador más corto para tablero 3x3
    utils.mostrar_tableros(mi_tablero, tablero_rival)

    # ── Turno del jugador ──────────────────────────────────────────────────────

    try:
        accion = input("🎯 Dispara (Fila Columna) o 'Q' para salir: ").lower()

        if accion == 'q':
            mensajes_rendicion = [
                "¿Te rindes? ¡Mira, detrás de ti, un mono de tres cabezas!",
                "¿Abandonas?... Sabía que ese traje de pirata te venía grande.",
                "¿Rendición? ¡Vuelve cuando hayas aprendido a insultar como un hombre!",
                "Error 404: valentía no encontrada. Vuelve cuando tengas agallas. 💀"
            ]
            print(random.choice(mensajes_rendicion))
            rendido = True
            break

        coords = accion.replace(",", " ").split()
        if len(coords) != 2:
            print("❌ Formato incorrecto. Ejemplo: 1 2")
            continue

        f, c = map(int, coords)

        if not (0 <= f <= 2 and 0 <= c <= 2):  # ← cambiado de 9 a 2
            print("🚫 Coordenadas fuera de rango. El tablero es de 0 a 2.")
            continue

        disparo = utils.disparar((f, c), tablero_rival_oculto, flota_rival)

        if disparo == "tocado":
            tablero_rival[f, c] = "X"
            jugador_gana = not np.any(tablero_rival_oculto == "O")  # ← compruebo victoria aquí
            if jugador_gana:
                break  # salgo del bucle inmediatamente sin pedir más disparos
            print("🎯 ¡Acertaste! Vuelves a disparar.")
            continue  # el jugador acierta → repite turno, el rival no dispara
        elif disparo == "agua":
            tablero_rival[f, c] = "A"

    except ValueError:
        print("⚠️ Introduce números válidos.")
        continue

    # ── Turno del rival ────────────────────────────────────────────────────────

    if disparo != "repetido":
        print("\n📡 Turno del enemigo... buscando señales radar...")
        time.sleep(1.5)

        f_aleatoria = np.random.randint(0, 3)  # ← cambiado de 10 a 3
        c_aleatoria = np.random.randint(0, 3)

        print(f"💥 El rival lanza un misil a ({f_aleatoria}, {c_aleatoria})")
        time.sleep(1)

        disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)

        # Si el rival acierta, sigue disparando
        while disparo_rival == "tocado":
            print("🔥 ¡El rival ha acertado y vuelve a disparar!")
            time.sleep(1.5)

            f_aleatoria = np.random.randint(0, 3)  # ← cambiado de 10 a 3
            c_aleatoria = np.random.randint(0, 3)
            print(f"💥 El rival repite disparo a ({f_aleatoria}, {c_aleatoria})")
            time.sleep(1)

            disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)

    # ── Compruebo si hay victoria ──────────────────────────────────────────────

    jugador_gana = not np.any(tablero_rival_oculto == "O")
    rival_gana = not np.any(mi_tablero == "O")

# RESULTADO

if not rendido:
    utils.mostrar_tableros(mi_tablero, tablero_rival)

    if jugador_gana:
        mensajes_victoria = [
            "¡Has ganado! Claramente mi flota lucha como una vaca.",
            "¡Increíble! Has hundido mis barcos más rápido que un grog barato en la garganta de un pirata.",
            "¡Hundidos! Tus disparos son más afilados que mi espada (que por cierto, está recién afilada)."
        ]
        print(random.choice(mensajes_victoria))
    elif rival_gana:
        mensajes_derrota = [
            "He hundido tu flota. Espero que te guste el fondo del mar, no hay mucho grog.",
            "¡He ganado! Al menos ahora tus barcos no tendrán que aguantar tu cara.",
            "¡Hundido! Mis disparos son tan certeros como mi dialéctica."
        ]
        print(random.choice(mensajes_derrota))