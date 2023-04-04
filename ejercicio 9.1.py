print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 31 de marzo del 2023\n")
print("Calificaciones Finales")
calificacion=float(input("Ingrese su calificación final: "))
if calificacion>=9.50 and calificacion<=10:
    print("Su calificación es excelente")
elif calificacion>=8.50 and calificacion<9.50:
    print("Su calificación es muy buena")
elif calificacion>=7.00 and calificacion<8.50:
    print("Su calificación es buena")
elif calificacion>=4.00 and calificacion<7.00:
    print("Su calificación es regular")
elif calificacion>=0.00 and calificacion<4.00:
    print("Su calificación es deficiente")
else:
    print("REPROBADO")