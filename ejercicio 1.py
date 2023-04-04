print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 30 de marzo del 2023\n")

semaforo=input("Ingrese el estado del semáforo: ")
if semaforo=="verde":
    print("El usuario puede cruzar la calle")
elif semaforo=="amarillo":
    print("El usuario no puede cruzar la calle")
elif semaforo=="rojo":
    print("El usuario no puede cruzar la calle")
else:
    print("El color ingresado no corresponde a los colores del semáforo")