print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
# Determinar el mayor de tres numeros.

a=int(input("Ingresar el primer número: "))
b=int(input("Ingresar el segundo número: "))
c=int(input("Ingresar el tercer número: "))

if a>b and a>c :
    print("El número ",a, "es mayor.")
elif b>a and b>c : 
    print("El número", b, " es mayor ")  
elif c>a and c>b:
    print("El número",c, "es mayor")
else:
    print("Ninguno es mayor ") 