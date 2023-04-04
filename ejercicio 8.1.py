print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 31 de marzo del 2023\n")
numero=input("Ingrese un número: ")
if len(numero) !=1:
    print("No se puede procesar el dato, debe ingresar un solo número")
elif numero in "123456789":
    print("El número",numero, "se encuentra dentro del rango")
else: 
    print("El número ingresado no se encuentra dentro del rango")