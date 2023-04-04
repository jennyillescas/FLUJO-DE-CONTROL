print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 01 de abril del 2023\n")
#Escribir un programa que pregunte al usuario una cantidad de días y muestre por pantalla cuantas:
# horas, minutos y segundos hay en dicha cantidad de días.

dias= int(input("Escriba una cantidad de días: "))
horas= dias * 24
minutos=horas*60
segundos=minutos*60 
 
print(dias,"días tiene",horas,"horas" ,minutos,"minutos""y",segundos,"segundos")