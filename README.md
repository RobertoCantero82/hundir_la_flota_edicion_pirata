<p align="center">
  <img src="img/banner.png" width="100%" alt="Hundir la Flota - Edición Vitoria-Gasteiz">
</p>

<h1 align="center">🏴‍☠️ Simulador de estrategia naval desarrollado en Python para el Bootcamp de Data Science de The Bridge  🏴‍☠️</h1>


## 🚩 Misión y Objetivos 🚩

Este proyecto no es solo una recreación del clásico juego de mesa. Este es el primer desafío de programación del bootcamp de Data Science para demostrar los conocimientos adquiridos en Python y Programación Orientada a Objetos. Gracias al proyecto he aprendido a:

1.  **Estructurar la lógica del código:** gestionando el proyecto en archivos y pensando las fases del juego para trasladarlas al lenguaje del ordenador.
2.  **Aplicar los conceptos aprendidos desde el inicio del bootcamp:** poniendo en práctica condicionales, bucles o la propia Programación Orientada a Objetos.
3.  **Conseguir crear un entorno de juego funcional y divertido:** no solo que el juego funcione, sino que siga las principales reglas del juego de mesa original, con divertidas características adicionales.

## ⚙️ Flujo de trabajo ⚙️

#### ⚓ Archivo principal (_hundirlaflota.py_)

1. Importación de librerías: las creadas para las funciones y clases, además de NumPy y Random.

2. Creación de los tableros (jugador, rival y el oculto del rival).

3. Colocación de los barcos para obtener la flota del jugador y la flota del rival.
   
4. Bucle del juego.
   
5. Resultado de la victoria/derrota. 

#### 📦 Archivo de la clase (_clases.py_)

1. Creación de la clase Barco: incluirá el tamaño (eslora), las coordenadas para situarlo en el tablero, las vidas y el nombre, que dependerá del tamaño.

2. Funciones: un barco puede recibir un impacto (lo que le quita una vida) o puede hundirse (cuando no tiene vidas).

#### 🔗 Archivo de funciones (_utils.py_)

1. Importo las librerías: la creada como clases, Random y NumPy.

2. Función para crear tableros.
   
3. Función para colorear las celdas.

4. Función para mostrar los tableros.
   
5. Función para colocar los barcos en el tablero del jugador.
   
6. Función para colocar los barcos en el tablero del rival.
   
7. Función para disparar.

## 📂 Distribución del repositorio

- En la ruta principal se encuentra hundirlaflota.py, que es el archivo principal que se ejecuta. Después están clases.py y utils.pys, que son los archivos que recogen las clases y las funciones, respectivamente.
- En la carpeta img, se incluyen las imágenes necesarias para adornar el repositorio.
- En la carpeta prueba se incluye una versión mini del juego, pensaba como banco de pruebas para comprobar que todo funciona correctamente y no tener que jugar una partida más larga.
