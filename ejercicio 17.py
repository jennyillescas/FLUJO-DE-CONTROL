print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
"""###7.
 Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
- 0-2: Muy deficiente
- 3-4: Insuficiente
- 5-6: Suficiente
- 7: Bien
- 8-9: Notable
- 10: Sobresaliente"""

calificacion=int(input("Ingrese su calificación: "))

if calificacion >= 0 and calificacion <=2:
    print("Su calificación de " , calificacion,"es MUY DEFICIENTE")
elif calificacion >= 3 and calificacion <= 4 :
    print("Su calificación de ", calificacion, " es INSUFICIENTE ")
elif calificacion >= 5 and calificacion <= 6:
    print("Su calificación de " , calificacion, "es SUFICIENTE ")
elif calificacion ==7  :
    print("Su calificación de " , calificacion," esta BIEN ")
elif calificacion >= 8 and calificacion <= 9:
    print("Su calificación de", calificacion," es NOTABLE ")
elif calificacion == 10 :
    print("Su calificación de " , calificacion, " es SOBRESALIENTE ")
else:
    print("El valor ingresado no esta dentro del rango de calificaciones ")
 
