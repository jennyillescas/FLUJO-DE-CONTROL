print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 31 de marzo del 2023\n")
valor_1=int(input("Ingrese el valor 1: "))
valor_2=int(input("Ingrese el valor 2: "))
print("Presione 1 para sumar")
print("Presione 2 para restar")
print("Presione 3 para multiplicar")
opción= int(input("Que opción desea:"))
if opción==1:
    print("La suma es: ",valor_1+valor_2)
elif opción==2:
    print("La resta es: ",valor_1-valor_2 )
elif opción==3:
    print("La multiplicación es: ",valor_1*valor_2)
else:
    print("La opción no es correcta")

   