"""Proyecto 3: Juego de Adivinanzas
• Descripción: Un juego interactivo donde el usuario 
debe adivinar un número generado aleatoriamente por 
el programa. Incorpora límites de intentos y proporciona
pistas.
• Objetivos de Aprendizaje: Estructuras de control, 
generación de números aleatorios, entrada/salida básica."""

import random

nr_random = random.randint(1,25)
intentos = 0

print("Intenta adivinar un numero entre el 1 y el 25 en cinco intentos")

while intentos < 5:
    print(f"Numero de Intentos {intentos}")
    intento = int(input())
    intentos += 1 
    if intento < nr_random:
        print("Tu numero es demasiado bajo")
    elif intento > nr_random:
        print("Tu numero es demasiado alto")
    else:
        break
    
if intento == nr_random:
    print(f"Has adivinado el numero, es {nr_random}")
else:
    print(f"Has perdido, el numero era {nr_random}")
