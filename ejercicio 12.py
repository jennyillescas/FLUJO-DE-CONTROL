print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
#Determine si un numero es negativo,positivo o cero

numero=int(input("Ingrese un número: "))

if numero > 0:
    print("El número",numero, "es positivo ")
elif numero < 0:
    print ("El número ", numero, "es negativo")
else:
    print("El número",numero, "es cero ")