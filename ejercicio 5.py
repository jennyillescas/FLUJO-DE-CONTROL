print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 31 de marzo del 2023\n")
impuesto=0
salario=float(input("Ingrese su salario: "))
if salario<10000:
    print("Se debe pagar el impuesto de 5%")
    impuesto=5/100
elif salario>=10000 and salario<20000:
    print("Se debe pagar el impuesto de 15%")
    impuesto=15/100
elif salario>=20000 and salario<35000:
    print("Se debe pagar el impuesto de 20%")
    impuesto=20/100
elif salario>=35000 and salario<60000:
    print("Se debe pagar el impuesto de 30%")
    impuesto=30/100
elif salario>=60000:
    print("Se debe pagar el impuesto de 45%")
    impuesto=45/100
else:
    print("El salario ingresado no es el correcto")
    
total=salario*impuesto
print("El valor del impuesto a pagar es de: ",total)
print("El salario a recibir es: ",salario-total)