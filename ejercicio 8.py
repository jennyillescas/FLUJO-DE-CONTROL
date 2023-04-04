print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 31 de marzo del 2023\n")
letra=input("Ingrese una letra: ")
if len(letra)!=1:
    print("No se puede procesar el dato, debe ingresar una sola letra")
elif letra in "aeiouAEIOU":
    print("Es una vocal")
else:
    print("No es una vocal")