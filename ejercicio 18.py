print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
"""###7.
Escribir un programa que pida al usuario una frase y determine si es un palíndromo. Ignorar espacios en blanco y mayúsculas/minúsculas
al determinar si la frase es un palíndromo o no.
-Un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
Por ejemplo, "ana", "radar" y "aibohphobia" son palíndromos."""

import re
frase=input("Escriba una frase o palabra: ")
frase=  re.sub(r'[^a-zA-Z]', '', frase).lower()
if frase == frase [:: -1]:
    print(" la frase o palabra",frase, "es un palíndromo")
else:
    print("La frase o palabra ",frase, " no es un palíndromo")