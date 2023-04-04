print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
año=int(input("Ingresar el año : "))
if año % 4 ==0 and año % 100 != 0 :
    print ("El año " , año, "es bisiesto ")
elif año % 400 ==0:
    print("El ", año, "es divisible entre 400 ")
else:
    print("El número ingresado no es bisiesto y por lo tanto no es divible entre los numeros propuestos ")